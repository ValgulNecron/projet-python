
use sqlx::SqlitePool;
const DATABASE_FILE: &str = "./db/data.db";
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
    sqlx::query("UPDATE account SET email = ?, password = ?, username = ?, updated_at = ? WHERE id = ?")
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

pub async fn get_account_by_mail(email: String) -> Option<sqlx::sqlite::SqliteRow> {
    let pool = get_pool().await;
    sqlx::query("SELECT id, email, username, password FROM account WHERE email = ?")
        .bind(email)
        .fetch_optional(&pool)
        .await
        .unwrap()
}