use std::collections::HashMap;
use std::sync::{Arc};
use tokio::sync::RwLock;
use tonic::{Request, Response, Status};
use crate::service::player_pos_service::proto::{GetAllPosRequest, GetAllPosResponse, GetPosRequest, GetPosResponse, UpdatePosRequest, UpdatePosResponse};
use crate::service::player_pos_service::proto::player_pos_service_server::{PlayerPosService, PlayerPosServiceServer};
use crate::service::state::check_token;

pub(crate) mod proto {
    tonic::include_proto!("player_pos");

    pub(crate) const FILE_DESCRIPTOR_SET: &[u8] =
        tonic::include_file_descriptor_set!("player_pos_descriptor");
}

struct UserPos {
    pub x: u64,
    pub y: u64,
    pub last_update: u64,
    pub velocity_y: f32,
    pub velocity_x: f32,
}

pub struct PlayerPos {
    pub(crate) users_pos: Arc<RwLock<HashMap<String, UserPos>>>,
    pub(crate) users_token: Arc<RwLock<HashMap<String, String>>>,
}

impl PlayerPosService for PlayerPos {
    async fn player_get_pos(&self, request: Request<GetPosRequest>) -> Result<Response<GetPosResponse>, Status> {
        let data = request.into_inner();
        if !check_token(data.token.as_str(), data.user_id.as_str(), &self.users_token).await {
            return Err(Status::unauthenticated("Invalid token"));
        }

        let actual_pos = match self.users_pos.read().await.get(&data.user_id) {
            Some(pos) => pos,
            None => return Err(Status::not_found("User not found")),
        };

        let response = GetPosResponse {
            pos: PlayerPos::proto::Pos {
                x: actual_pos.x,
                y: actual_pos.y,
            },
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

        let mut users_pos = self.users_pos.write().await;
        users_pos.insert(data.user_id, UserPos {
            x: pos.pos_x,
            y: pos.pos_y,
            last_update: pos.last_update,
            velocity_y: pos.velocity_y,
            velocity_x: pos.velocity_x,
        });

        Ok(Response::new(UpdatePosResponse { success: true }))
    }

    async fn player_get_all_pos(&self, request: Request<GetAllPosRequest>) -> Result<Response<GetAllPosResponse>, Status> {
        todo!()
    }
}