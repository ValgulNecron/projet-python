use crate::service::account_services::{
    get_account_service, AccountService,
};
use crate::service::state::AccountToken;
use base64::Engine as _;
use sqlx::Row;
use tonic::transport::Server;

use crate::sqlite::db::create_database_and_database_file;

mod service;
mod sqlite;

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
        .register_encoded_file_descriptor_set(service::account_services::proto::FILE_DESCRIPTOR_SET)
        .build()?;
    Server::builder()
        .add_service(service)
        .add_service(get_account_service(account_service))
        .serve(addr)
        .await?;
    println!("Server running on {}", addr);
    Ok(())
}
