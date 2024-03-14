use std::collections::HashMap;
use std::sync::Arc;
use tokio::sync::RwLock;

pub(crate) type AccountToken = Arc<RwLock<HashMap<String, String>>>;

pub async fn check_token(token: &str, id: &str, users_token: &AccountToken) -> bool {
    match users_token.read().await.get(id) {
        Some(t) => t == token,
        None => false,
    }
}
