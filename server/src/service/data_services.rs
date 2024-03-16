use tonic::{Request, Response, Status};
use crate::service::data_services::proto::{AddUserDataRequest, AddUserDataResponse, DeleteUserDataRequest, DeleteUserDataResponse, GetItemListRequest, GetItemListResponse, GetItemRequest, GetItemResponse, GetMapDataRequest, GetMapDataResponse, GetUserDataRequest, GetUserDataResponse, UpdateUserDataRequest, UpdateUserDataResponse};
use crate::service::data_services::proto::map_data_server::MapData;
use crate::service::data_services::proto::user_data_server::UserData;
use crate::service::state::AccountToken;
use crate::service::data_services::proto::item_data_server::ItemData;
pub(crate) mod proto {
    tonic::include_proto!("data");

    pub(crate) const FILE_DESCRIPTOR_SET: &[u8] =
        tonic::include_file_descriptor_set!("data_descriptor");
}

#[derive(Debug, Default)]
struct Data {
    pub(crate) users_token: AccountToken,
}

#[tonic::async_trait]
impl UserData for Data {
    async fn get_user_data(&self, request: Request<GetUserDataRequest>) -> Result<Response<GetUserDataResponse>, Status> {
        todo!()
    }

    async fn add_user_data(&self, request: Request<AddUserDataRequest>) -> Result<Response<AddUserDataResponse>, Status> {
        todo!()
    }

    async fn update_user_data(&self, request: Request<UpdateUserDataRequest>) -> Result<Response<UpdateUserDataResponse>, Status> {
        todo!()
    }

    async fn delete_user_data(&self, request: Request<DeleteUserDataRequest>) -> Result<Response<DeleteUserDataResponse>, Status> {
        todo!()
    }
}

#[tonic::async_trait]
impl ItemData for Data {
    async fn get_item_list(&self, request: Request<GetItemListRequest>) -> Result<Response<GetItemListResponse>, Status> {
        todo!()
    }
    async fn get_item(&self, request: Request<GetItemRequest>) -> Result<Response<GetItemResponse>, Status> {
        todo!()
    }
}

#[tonic::async_trait]
impl MapData for Data {
    async fn get_map_data(&self, request: Request<GetMapDataRequest>) -> Result<Response<GetMapDataResponse>, Status> {
        todo!()
    }
}