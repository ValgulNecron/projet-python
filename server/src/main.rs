use std::collections::HashMap;
use std::sync::Arc;
use tokio::sync::RwLock;
use crate::service::account_services::{
    get_account_service, AccountService,
};
use tonic::transport::Server;
use crate::service::data_services::{DataService, get_item_service, get_map_service, get_user_service, load_all_item_from_json};
use std::fs;
use std::path::Path;
use std::process::Command;
use rcgen::{Certificate, RcgenError};
use crate::service::player_pos_service::{get_pos_service, PlayerPosServerService, UserPos};

use crate::sqlite::db::create_database_and_database_file;

mod service;
mod sqlite;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    println!("Server running");
    create_database_and_database_file().await;
    let addr = "0.0.0.0:3333".parse().expect("Invalid address");
    let account_token: Arc<RwLock<HashMap<String, String>>> = Arc::new(RwLock::new(HashMap::new()));

    let account_service = AccountService {
        users_token: account_token.clone(),
    };

    let map = load_all_item_from_json();
    let data_service_item = DataService {
        users_token: account_token.clone(),
        items: map,
    };
    let map = load_all_item_from_json();
    let data_service_map = DataService {
        users_token: account_token.clone(),
        items: map,
    };
    let map = load_all_item_from_json();
    let data_service_user = DataService {
        users_token: account_token.clone(),
        items: map,
    };

    let mut users_pos: Arc<RwLock<HashMap<String, UserPos>>> = Arc::new(RwLock::new(HashMap::new()));
    let player_pos = PlayerPosServerService {
        users_pos: users_pos.clone(),
        users_token: account_token.clone(),
    };

    // run the cleaner function in a separate task
    tokio::spawn(cleaner(account_token.clone(), users_pos.clone()));

    let reflection = tonic_reflection::server::Builder::configure()
        .register_encoded_file_descriptor_set(service::account_services::proto::FILE_DESCRIPTOR_SET)
        .register_encoded_file_descriptor_set(service::data_services::proto::FILE_DESCRIPTOR_SET)
        .build()?;
    Server::builder()
        .add_service(reflection)
        .add_service(get_account_service(account_service))
        .add_service(get_item_service(data_service_item))
        .add_service(get_map_service(data_service_map))
        .add_service(get_user_service(data_service_user))
        .add_service(get_pos_service(player_pos))
        .serve(addr)
        .await?;
    println!("Server running on {}", addr);
    Ok(())
}

async fn cleaner(users_token: Arc<RwLock<HashMap<String, String>>>, player_pos: Arc<RwLock<HashMap<String, UserPos>>>) {
    loop {
        let actual_pos = player_pos.read().await;
        let actual_pos = actual_pos.clone();
        for (id, pos) in &actual_pos {
            if pos.last_update + 600 < chrono::Utc::now().timestamp() as u64 {
                let mut actual_pos = player_pos.write().await;
                actual_pos.remove(id);
                let mut actual_token = users_token.write().await;
                actual_token.remove(id);
            }
        }
    }
}