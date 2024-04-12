use std::collections::HashMap;
use std::sync::Arc;
use tokio::sync::RwLock;

pub async fn check_token(token: &str, id: &str, users_token: &Arc<RwLock<HashMap<String, String>>>) -> bool {
    match users_token.read().await.get(id) {
        Some(t) => t == token,
        None => false,
    }
}
