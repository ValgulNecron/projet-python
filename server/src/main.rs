mod sqlite;

use std::num::NonZeroU32;
use ring::pbkdf2;
use proto::account_server::{Account, AccountServer};
use uuid::Uuid;
use rand::{random, Rng};
use tonic::{Request, Response, Status};
use crate::proto::{DeleteAccountRequest, DeleteAccountResponse, LoginRequest, LoginResponse, UpdateAccountRequest, UpdateAccountResponse};
use crate::sqlite::db::{create_account, create_database_and_database_file, get_account};
use base64::{engine::general_purpose, Engine as _};
use sqlx::Row;
use tonic::transport::Server;

mod proto {
    tonic::include_proto!("account");

    pub(crate) const FILE_DESCRIPTOR_SET: &[u8] =
        tonic::include_file_descriptor_set!("account_descriptor");
}

#[derive(Debug, Default)]
pub struct AccountService {}

fn hash_password(password: &[u8], salt: &[u8]) -> String {
    let mut output = [0u8;  1024]; // Example output size
    pbkdf2::derive(
        pbkdf2::PBKDF2_HMAC_SHA512,
        NonZeroU32::new(100_000).unwrap(), // Number of iterations
        &salt,
        password,
        &mut output,
    );
    general_purpose::STANDARD.encode(&output)
}

#[tonic::async_trait]
impl Account for AccountService {
    async fn create_account(
        &self,
        request: Request<proto::CreateAccountRequest>,
    ) -> Result<Response<proto::CreateAccountResponse>, Status> {
        let id = Uuid::new_v4();
        println!("Got a request: {:?}", request);
        let data = request.into_inner();
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
        request: Request<proto::GetAccountRequest>,
    ) -> Result<Response<proto::GetAccountResponse>, Status> {
        println!("Got a request: {:?}", request);
        let data = request.into_inner();
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
        todo!()
    }

    async fn delete_account(&self, request: Request<DeleteAccountRequest>) -> Result<Response<DeleteAccountResponse>, Status> {
        todo!()
    }

    async fn login(&self, request: Request<LoginRequest>) -> Result<Response<LoginResponse>, Status> {
        todo!()
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    create_database_and_database_file().await;
    let addr = "0.0.0.0:3333".parse().unwrap();
    let account_service = AccountService::default();

    let service = tonic_reflection::server::Builder::configure()
        .register_encoded_file_descriptor_set(proto::FILE_DESCRIPTOR_SET)
        .build()?;
    Server::builder()
        .add_service(service)
        .add_service(AccountServer::new(account_service))
        .serve(addr)
        .await?;
    Ok(())
}
