mod sqlite;

use std::collections::HashMap;
use std::num::NonZeroU32;
use std::sync::Arc;
use ring::pbkdf2;
use proto::account_server::{Account, AccountServer};
use uuid::Uuid;
use rand::{random};
use tonic::{Request, Response, Status};
use crate::proto::{DeleteAccountRequest, DeleteAccountResponse, GetAccountRequest, LoginRequest, LoginResponse, UpdateAccountRequest, UpdateAccountResponse};
use crate::sqlite::db::{create_account, create_database_and_database_file, delete_account, entry_exists, get_account, get_account_by_mail, update_account};
use base64::{engine::general_purpose, Engine as _};
use sqlx::Row;
use tokio::sync::RwLock;
use tonic::transport::Server;

type AccountToken = Arc<RwLock<HashMap<String, String>>>;

mod proto {
    tonic::include_proto!("account");

    pub(crate) const FILE_DESCRIPTOR_SET: &[u8] =
        tonic::include_file_descriptor_set!("account_descriptor");
}

async fn check_token(token: &str, id: &str, users_token: &AccountToken) -> bool {
    match users_token.read().await.get(id) {
        Some(t) => t == token,
        None => false,
    }
}

#[derive(Debug, Default)]
pub struct AccountService {
    users_token: AccountToken,
}

impl AccountService {
    pub async fn add_token(&self, id: String, token: String) {
     let mut users_token = self.users_token.write().await;
        users_token.insert(id, token);

    }

}

fn hash_password(password: &[u8], salt: &[u8]) -> String {
    let mut output = [0u8;  1024]; // Example output size
    pbkdf2::derive(
        pbkdf2::PBKDF2_HMAC_SHA512,
        NonZeroU32::new(100_000).unwrap(), // Number of iterations
        salt,
        password,
        &mut output,
    );
    let out = general_purpose::STANDARD.encode(output);
    let salt = general_purpose::STANDARD.encode(salt);
    format!("pbkdf2_sha512${}${}${}", 100_000, salt, out)
}

fn verify_password(password: &[u8], hash: &str) -> bool {
    let parts: Vec<&str> = hash.split('$').collect();
    let saved_hash = parts[3];
    let salt = general_purpose::STANDARD.decode(parts[2].as_bytes()).unwrap();
    let hash = hash_password(password, salt.as_ref());
    hash == saved_hash
}

#[tonic::async_trait]
impl Account for AccountService {
    async fn create_account(
        &self,
        request: Request<proto::CreateAccountRequest>,
    ) -> Result<Response<proto::CreateAccountResponse>, Status> {
        let data = request.into_inner();
        if entry_exists(data.email.as_str(), data.username.as_str()) {
            return Err(Status::already_exists("This entry already exist."))
        }
        let id = Uuid::new_v4();
        println!("Got a request: {:?}", request);
        let salt = random::<[u8; 32]>();
        let salt = salt.as_ref();
        let password = hash_password(data.password.as_ref(), salt);
        create_account(id.to_string(), data.email, password, data.username).await;

        let response = proto::CreateAccountResponse {
            id: id.to_string(),
            created: true,
        };

        Ok(Response::new(response))
    }

    async fn get_account(
        &self,
        request: Request<GetAccountRequest>,
    ) -> Result<Response<proto::GetAccountResponse>, Status> {
        let data = request.into_inner();
        if !check_token(data.token.as_str(), data.id.as_str(), &self.users_token).await {
            return Err(Status::unauthenticated("Invalid token"));
        }
        let row = get_account(data.id).await.unwrap();
        let response = proto::GetAccountResponse {
            id: row.get(0),
            email: row.get(1),
            username: row.get(2),
            created: row.get(3),
            updated: row.get(4),
        };
        Ok(Response::new(response))
    }

    async fn update_account(&self, request: Request<UpdateAccountRequest>) -> Result<Response<UpdateAccountResponse>, Status> {
        let data = request.into_inner();
        if !check_token(data.token.as_str(), data.id.as_str(), &self.users_token).await {
            return Err(Status::unauthenticated("Invalid token"));
        }
        let id = data.id.clone();
        let salt = random::<[u8; 32]>();
        let salt = salt.as_ref();
        let password = hash_password(data.password.as_ref(), salt);
        update_account(id.clone(), data.email, password, data.username).await;
        let response = UpdateAccountResponse {
            id,
            updated: true,
        };
        Ok(Response::new(response))
    }

    async fn delete_account(&self, request: Request<DeleteAccountRequest>) -> Result<Response<DeleteAccountResponse>, Status> {
        let data = request.into_inner();
        if !check_token(data.token.as_str(), data.id.as_str(), &self.users_token).await {
            return Err(Status::unauthenticated("Invalid token"));
        }
        let id = data.id.clone();
        delete_account(data.id).await;

        let response = DeleteAccountResponse {
            id,
            deleted: true,
        };
        Ok(Response::new(response))
    }

    async fn login(&self, request: Request<LoginRequest>) -> Result<Response<LoginResponse>, Status> {
        let data = request.into_inner();
        let row = match get_account_by_mail(data.email).await {
            Some(row) => row,
            None => return Err(Status::unauthenticated("Invalid password or email")),
        };
        let password: String = row.get(3);
        let same_password = verify_password(data.password.as_ref(), password.as_str());
        let id: String = row.get(0);
        if !same_password {
            return Err(Status::unauthenticated("Invalid password or email"));
        }

        let token = Uuid::new_v4().to_string();
        self.add_token(id.clone(), token.clone()).await;
        let response = LoginResponse {
            id,
            logged: true,
            token,
        };
        Ok(Response::new(response))
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    println!("Server running");
    create_database_and_database_file().await;
    let addr = "0.0.0.0:3333".parse().unwrap();
    let account_token = AccountToken::default();

    let account_service = AccountService {
        users_token: account_token.clone(),
    };

    let service = tonic_reflection::server::Builder::configure()
        .register_encoded_file_descriptor_set(proto::FILE_DESCRIPTOR_SET)
        .build()?;
    Server::builder()
        .add_service(service)
        .add_service(AccountServer::new(account_service))
        .serve(addr)
        .await?;
    println!("Server running on {}", addr);
    Ok(())
}
