use crate::service::account_services::{
    get_account_service, AccountService,
};
use crate::service::state::AccountToken;
use tonic::transport::Server;
use crate::service::data_services::{DataService, get_item_service, get_map_service, get_user_service, load_all_item_from_json};

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

    //let map = load_all_item_from_json();
    /*let data_service = DataService {
        users_token: account_token.clone(),
        items: map,
    };*/

    let reflection = tonic_reflection::server::Builder::configure()
        .register_encoded_file_descriptor_set(service::account_services::proto::FILE_DESCRIPTOR_SET)
        //.register_encoded_file_descriptor_set(service::data_services::proto::FILE_DESCRIPTOR_SET)
        .build()?;
    Server::builder()
        .add_service(reflection)
        .add_service(get_account_service(account_service))
        /*.add_service(get_item_service(data_service.clone()))
        .add_service(get_map_service(data_service.clone()))
        .add_service(get_user_service(data_service))*/
        .serve(addr)
        .await?;
    println!("Server running on {}", addr);
    Ok(())
}
