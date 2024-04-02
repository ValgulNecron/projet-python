use std::collections::HashMap;
use std::fs;
use tonic::{Request, Response, Status};
use serde::{Deserialize, Serialize};
use sqlx::Row;
use crate::service::data_services::proto::{AddUserDataRequest, AddUserDataResponse, DeleteUserDataRequest, DeleteUserDataResponse, GetItemListRequest, GetItemListResponse, GetItemRequest, GetItemResponse, GetMapDataRequest, GetMapDataResponse, GetUserDataRequest, GetUserDataResponse, Item, UpdateUserDataRequest, UpdateUserDataResponse};
use crate::service::data_services::proto::map_data_server::{MapData, MapDataServer};
use crate::service::data_services::proto::user_data_server::{UserData, UserDataServer};
use crate::service::state::{AccountToken, check_token};
use crate::service::data_services::proto::item_data_server::{ItemData, ItemDataServer};
use crate::sqlite::db::{add_user_data, delete_user_data, get_all_user_data};

const TMX_FILE: &str = "./data/map.tmx";
const TSX_FILE: &str = "./data/terrain_atlas.tsx";
const PNG_FILE: &str = "./data/terrain_atlas.png";

const ITEM_FILE: &str = "./data/item.json";

pub(crate) mod proto {
    tonic::include_proto!("data");

    pub(crate) const FILE_DESCRIPTOR_SET: &[u8] =
        tonic::include_file_descriptor_set!("data_descriptor");
}

#[derive(Debug, Default, Clone)]
pub struct DataService {
    pub(crate) users_token: AccountToken,
    pub(crate) items: HashMap<String, RealItem>,
}

#[tonic::async_trait]
impl UserData for DataService {
    async fn get_user_data(&self, request: Request<GetUserDataRequest>) -> Result<Response<GetUserDataResponse>, Status> {
        let data = request.into_inner();
        if !check_token(data.token.as_str(), data.user_id.as_str(), &self.users_token).await {
            return Err(Status::unauthenticated("Invalid token"));
        }
        let user_data = get_all_user_data(data.user_id.as_str()).await;

        Ok(Response::new(GetUserDataResponse {
            items: user_data.into_iter().map(|data| {
                let item_id = data.1.unwrap_or_default();
                let slot = data.2.unwrap_or_default();
                let item = self.items.get(&item_id).unwrap();
                Item {
                    id: item.id.clone(),
                    nom: item.nom.clone(),
                    force: item.force,
                    endurance: item.endurance,
                    intelligence: item.intelligence,
                    vitalite: item.vitalite,
                    mana: item.mana,
                    rarete: item.rarete.clone(),
                    vitesse: item.vitesse.unwrap_or(0.0),
                    sprite: item.sprite.clone(),
                    slot,
                }
            }).collect()
        }))
    }

    async fn add_user_data(&self, request: Request<AddUserDataRequest>) -> Result<Response<AddUserDataResponse>, Status> {
        let data = request.into_inner();
        if !check_token(data.token.as_str(), data.user_id.as_str(), &self.users_token).await {
            return Err(Status::unauthenticated("Invalid token"));
        }

        let item = match data.item {
            Some(item) => item,
            None => return Err(Status::invalid_argument("Item is required."))
        };

        if !add_user_data(data.user_id.as_str(), item.id.as_str() ,item.slot as i32).await {
            return Err(Status::internal("Failed to add user data."));
        };

        Ok(Response::new(AddUserDataResponse {
            success: true,
        }))
    }

    async fn update_user_data(&self, request: Request<UpdateUserDataRequest>) -> Result<Response<UpdateUserDataResponse>, Status> {
        let data = request.into_inner();
        if !check_token(data.token.as_str(), data.user_id.as_str(), &self.users_token).await {
            return Err(Status::unauthenticated("Invalid token"));
        }

        let item = match data.new_item {
            Some(item) => item,
            None => return Err(Status::invalid_argument("Item is required."))
        };

        if !add_user_data(data.user_id.as_str(), item.id.as_str() ,item.slot as i32).await {
            return Err(Status::internal("Failed to add user data."));
        };

        Ok(Response::new(UpdateUserDataResponse {
            success: true,
        }))
    }

    async fn delete_user_data(&self, request: Request<DeleteUserDataRequest>) -> Result<Response<DeleteUserDataResponse>, Status> {
        let data = request.into_inner();
        if !check_token(data.token.as_str(), data.user_id.as_str(), &self.users_token).await {
            return Err(Status::unauthenticated("Invalid token"));
        }

        let item = match data.item {
            Some(item) => item,
            None => return Err(Status::invalid_argument("Item is required."))
        };

        if !delete_user_data(data.user_id.as_str(), item.id.as_str()).await {
            return Err(Status::internal("Failed to add user data."));
        };

        Ok(Response::new(DeleteUserDataResponse {
            success: true,
        }))
    }
}

#[tonic::async_trait]
impl ItemData for DataService {
    async fn get_item_list(&self, request: Request<GetItemListRequest>) -> Result<Response<GetItemListResponse>, Status> {
        let data = request.into_inner();
        if !check_token(data.token.as_str(), data.user_id.as_str(), &self.users_token).await {
            return Err(Status::unauthenticated("Invalid token"));
        }
        Ok(Response::new(GetItemListResponse {
            items: self.items.values().map(|item| item.into()).collect()
        }))
    }

    async fn get_item(&self, request: Request<GetItemRequest>) -> Result<Response<GetItemResponse>, Status> {
        let data = request.into_inner();
        if !check_token(data.token.as_str(), data.user_id.as_str(), &self.users_token).await {
            return Err(Status::unauthenticated("Invalid token"));
        }
        let id = data.item_id;
        match self.items.get(&id) {
            Some(item) => Ok(Response::new(GetItemResponse {item: Some(item.into())})),
            None => Err(Status::not_found("Item not found."))
        }
    }
}

#[tonic::async_trait]
impl MapData for DataService {
    async fn get_map_data(&self, request: Request<GetMapDataRequest>) -> Result<Response<GetMapDataResponse>, Status> {
        let data = request.into_inner();
        if !check_token(data.token.as_str(), data.user_id.as_str(), &self.users_token).await {
            return Err(Status::unauthenticated("Invalid token"));
        }
        let map_tmx = match fs::read(TMX_FILE) {
            Ok(file) => file,
            Err(_) => return Err(Status::internal("Map file not found."))
        };
        let terrain_atlas_tsx = match fs::read(TSX_FILE) {
            Ok(file) => file,
            Err(_) => return Err(Status::internal("Atlas tsx file not found."))
        };
        let terrain_atlas_png = match fs::read(TMX_FILE) {
            Ok(file) => file,
            Err(_) => return Err(Status::internal("Atlas png file not found."))
        };
        Ok(Response::new(GetMapDataResponse {
            map_tmx,
            terrain_atlas_tsx,
            terrain_atlas_png,
        }))
    }
}

pub fn get_item_service(account_service: DataService) -> ItemDataServer<DataService> {
    ItemDataServer::new(account_service)
}

pub fn get_map_service(account_service: DataService) -> MapDataServer<DataService> {
    MapDataServer::new(account_service)
}

pub fn get_user_service(account_service: DataService) -> UserDataServer<DataService> {
    UserDataServer::new(account_service)
}

pub fn load_all_item_from_json() -> HashMap<String, RealItem> {
    let content = fs::read_to_string(ITEM_FILE).expect("Failed to read item file.");
    let items: ItemTempTempUseless = serde_json::from_str(&content).expect("Failed to parse item file.");
    let items = items.weapons;
    // add it to a hashmap with it id as key
    let new_items: Vec<RealItem> = items.into_iter().map(|item| {
        RealItem {
            id: item.id,
            nom: item.nom,
            force: item.force,
            endurance: item.endurance,
            intelligence: item.intelligence,
            vitalite: item.vitalite,
            mana: item.mana,
            rarete: item.rarete,
            vitesse: item.vitesse,
            sprite: {
                let path = format!("./data/sprite/{}", item.sprite);
                let content = fs::read(path).unwrap_or(vec![]);
                content
            },
            slot: item.slot,
        }
    }).collect();
    let mut map = HashMap::new();
    for item in new_items {
        map.insert(item.id.clone(), item);
    }
    map
}
#[derive(Clone, PartialEq, Deserialize, Serialize, Debug)]
pub struct ItemTempTempUseless {
    pub weapons: Vec<ItemTemp>,
}

#[derive(Clone, PartialEq, Deserialize, Serialize, Debug)]
pub struct ItemTemp {
    pub id: String,
    pub nom: String,
    pub force: i64,
    pub endurance: i64,
    pub intelligence: i64,
    pub vitalite: i64,
    pub mana: i64,
    pub rarete: String,
    pub vitesse: Option<f32>,
    pub sprite: String,
    pub slot: Option<i64>,
}

#[derive(Clone, PartialEq, Deserialize, Serialize, Debug)]
pub struct RealItem {
    pub id: String,
    pub nom: String,
    pub force: i64,
    pub endurance: i64,
    pub intelligence: i64,
    pub vitalite: i64,
    pub mana: i64,
    pub rarete: String,
    pub vitesse: Option<f32>,
    pub sprite: Vec<u8>,
    pub slot: Option<i64>,
}


impl From<RealItem> for Item {
    fn from(item: RealItem) -> Self {
        Item {
            id: item.id,
            nom: item.nom,
            force: item.force,
            endurance: item.endurance,
            intelligence: item.intelligence,
            vitalite: item.vitalite,
            mana: item.mana,
            rarete: item.rarete.clone(),
            vitesse: item.vitesse.unwrap_or(0.0),
            sprite: item.sprite.clone(),
            slot: item.slot.unwrap_or(0),
        }
    }
}

impl From<Item> for RealItem {
    fn from(item: Item) -> Self {
        RealItem {
            id: item.id,
            nom: item.nom,
            force: item.force,
            endurance: item.endurance,
            intelligence: item.intelligence,
            vitalite: item.vitalite,
            mana: item.mana,
            rarete: item.rarete.clone(),
            vitesse: Option::from(item.vitesse),
            sprite: item.sprite.clone(),
            slot: Option::from(item.slot),
        }
    }
}

impl From<&Item> for RealItem {
    fn from(item: &Item) -> Self {
        RealItem {
            id: item.id.clone(),
            nom: item.nom.clone(),
            force: item.force,
            endurance: item.endurance,
            intelligence: item.intelligence,
            vitalite: item.vitalite,
            mana: item.mana,
            rarete: item.rarete.clone(),
            vitesse: Option::from(item.vitesse),
            sprite: item.sprite.clone(),
            slot: Option::from(item.slot),
        }
    }
}

impl From<&RealItem> for Item {
    fn from(item: &RealItem) -> Self {
        Item {
            id: item.id.clone(),
            nom: item.nom.clone(),
            force: item.force,
            endurance: item.endurance,
            intelligence: item.intelligence,
            vitalite: item.vitalite,
            mana: item.mana,
            rarete: item.rarete.clone(),
            vitesse: item.vitesse.unwrap_or(0.0),
            sprite: item.sprite.clone(),
            slot: item.slot.unwrap_or(0),
        }
    }
}