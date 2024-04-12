use std::collections::HashMap;
use std::sync::{Arc};
use tokio::sync::RwLock;
use tonic::{Request, Response, Status};
use crate::service::player_pos_service::proto::{GetAllPosRequest, GetAllPosResponse, GetPosRequest, GetPosResponse, Pos,
                                                UpdatePosRequest, UpdatePosResponse, PosWrapper};
use crate::service::player_pos_service::proto::player_pos_service_server::{PlayerPosService, PlayerPosServiceServer};
use crate::service::state::check_token;

pub(crate) mod proto {
    tonic::include_proto!("player_pos");

    pub(crate) const FILE_DESCRIPTOR_SET: &[u8] =
        tonic::include_file_descriptor_set!("player_pos_descriptor");
}

#[derive(Debug, Default, Clone)]
pub struct UserPos {
    pub x: u64,
    pub y: u64,
    pub last_update: u64,
}

pub struct PlayerPosServerService {
    pub(crate) users_pos: Arc<RwLock<HashMap<String, UserPos>>>,
    pub(crate) users_token: Arc<RwLock<HashMap<String, String>>>,
}

#[tonic::async_trait]
impl PlayerPosService for PlayerPosServerService {
    async fn player_get_pos(&self, request: Request<GetPosRequest>) -> Result<Response<GetPosResponse>, Status> {
        let data = request.into_inner();
        if !check_token(data.token.as_str(), data.user_id.as_str(), &self.users_token).await {
            return Err(Status::unauthenticated("Invalid token"));
        }

        let actual_pos = &self.users_pos.read().await;
        let actual_pos = match actual_pos.get(&data.user_id).clone() {
            Some(pos) => pos,
            None => return Err(Status::not_found("User not found")),
        };

        let response = GetPosResponse {
            user_id: data.user_id,
            pos: Some(Pos {
                pos_x: actual_pos.x.clone(),
                pos_y: actual_pos.y.clone(),
                last_update: actual_pos.last_update.clone(),
            }),
        };
        Ok(Response::new(response))
    }

    async fn player_update_pos(&self, request: Request<UpdatePosRequest>) -> Result<Response<UpdatePosResponse>, Status> {
        let data = request.into_inner();
        if !check_token(data.token.as_str(), data.user_id.as_str(), &self.users_token).await {
            return Err(Status::unauthenticated("Invalid token"));
        }

        let pos = match data.pos {
            Some(pos) => pos,
            None => return Err(Status::invalid_argument("Invalid position data")),
        };

        let last_update = chrono::Utc::now().timestamp();

        let mut users_pos = self.users_pos.write().await;
        users_pos.insert(data.user_id, UserPos {
            x: pos.pos_x,
            y: pos.pos_y,
            last_update: last_update as u64,
        });

        Ok(Response::new(UpdatePosResponse { success: true }))
    }

    async fn player_get_all_pos(&self, request: Request<GetAllPosRequest>) -> Result<Response<GetAllPosResponse>, Status> {
        let data = request.into_inner();
        if !check_token(data.token.as_str(), data.user_id.as_str(), &self.users_token).await {
            return Err(Status::unauthenticated("Invalid token"));
        }

        // iter all users and get their positions
        let users_pos = self.users_pos.read().await;
        let mut all_pos = Vec::new();
        for (user_id, pos) in users_pos.iter() {
            all_pos.push(PosWrapper {
                user_id: user_id.clone(),
                pos: Some(Pos {
                    pos_x: pos.x.clone(),
                    pos_y: pos.y.clone(),
                    last_update: pos.last_update.clone(),
                }),
            });
        }

        Ok(Response::new(GetAllPosResponse { pos: all_pos }))
    }
}

pub fn get_pos_service(player_pos_server_service: PlayerPosServerService) -> PlayerPosServiceServer<PlayerPosServerService> {
    PlayerPosServiceServer::new(player_pos_server_service)
}