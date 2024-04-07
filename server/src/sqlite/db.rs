use std::error::Error;
use sqlx::{Row, SqlitePool};

const DATABASE_FILE: &str = "./data/data.db";

async fn get_pool() -> SqlitePool {
    SqlitePool::connect(DATABASE_FILE).await.unwrap()
}

pub async fn create_database_and_database_file() {
    std::fs::create_dir_all("./db").unwrap();
    let path = DATABASE_FILE;
    if !std::path::Path::new(path).exists() {
        std::fs::File::create(path).unwrap();
    }
    let pool = get_pool().await;
    sqlx::query("CREATE TABLE IF NOT EXISTS account (id TEXT PRIMARY KEY, email TEXT, password TEXT, username TEXT, created_at TEXT, updated_at TEXT)")
        .execute(&pool)
        .await
        .unwrap();

    sqlx::query("
            CREATE TABLE IF NOT EXISTS user_data (
                user_id TEXT,
                item_id TEXT,
                slot INTEGER,
                PRIMARY KEY (user_id, item_id)
            )
        "
    )
        .execute(&pool)
        .await
        .unwrap();

}

pub async fn create_account(id: String, email: String, password: String, username: String) {
    let pool = get_pool().await;
    sqlx::query("INSERT INTO account (id, email, password, username, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)")
        .bind(id)
        .bind(email)
        .bind(password)
        .bind(username)
        .bind(chrono::Utc::now().to_rfc3339())
        .bind(chrono::Utc::now().to_rfc3339())
        .execute(&pool)
        .await
        .unwrap();
}

pub async fn get_account(id: String) -> Option<sqlx::sqlite::SqliteRow> {
    let pool = get_pool().await;

    sqlx::query("SELECT id, email, username, created_at, updated_at FROM account WHERE id = ?")
        .bind(id)
        .fetch_optional(&pool)
        .await
        .unwrap()
}

pub async fn update_account(id: String, email: String, password: String, username: String) {
    let pool = get_pool().await;
    sqlx::query(
        "UPDATE account SET email = ?, password = ?, username = ?, updated_at = ? WHERE id = ?",
    )
    .bind(email)
    .bind(password)
    .bind(username)
    .bind(chrono::Utc::now().to_rfc3339())
    .bind(id)
    .execute(&pool)
    .await
    .unwrap();
}

pub async fn delete_account(id: String) {
    let pool = get_pool().await;
    sqlx::query("DELETE FROM account WHERE id = ?")
        .bind(id)
        .execute(&pool)
        .await
        .unwrap();
}

pub async fn get_account_by_username(email: String) -> Option<sqlx::sqlite::SqliteRow> {
    let pool = get_pool().await;
    sqlx::query("SELECT id, email, username, password FROM account WHERE username = ?")
        .bind(email)
        .fetch_optional(&pool)
        .await
        .unwrap()
}

pub async fn entry_exists(email: &str, username: &str) -> bool {
    let pool = get_pool().await;
    let row_exists =
        sqlx::query("SELECT EXISTS(SELECT 1 FROM account WHERE email = ? OR username = ?)")
            .bind(email)
            .bind(username)
            .fetch_one(&pool)
            .await
            .unwrap();

    row_exists.get::<bool, _>(0)
}

pub async fn get_all_user_data(user_id: &str) -> Vec<(Option<String>, Option<String>, Option<i64>)> {
    let pool = get_pool().await;
    sqlx::query_as("SELECT user_id, item_id, slot FROM user_data WHERE user_id = ?")
        .bind(user_id)
        .fetch_all(&pool)
        .await
        .unwrap()
}

pub async fn add_user_data(user_id: &str, item_id: &str, slot: i32) -> bool {
    let pool = get_pool().await;
    sqlx::query("INSERT OR REPLACE INTO user_data (user_id, item_id, slot) VALUES (?, ?, ?)")
        .bind(user_id)
        .bind(item_id)
        .bind(slot)
        .execute(&pool)
        .await
        .unwrap();
    true
}

pub async fn delete_user_data(user_id: &str, item_id: &str) -> bool {
    let pool = get_pool().await;
    sqlx::query("DELETE FROM user_data WHERE user_id = ? AND item_id = ?")
        .bind(user_id)
        .bind(item_id)
        .execute(&pool)
        .await
        .unwrap();
    true
}