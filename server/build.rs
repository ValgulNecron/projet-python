use std::error::Error;
use std::{env, path::PathBuf};

fn main() -> Result<(), Box<dyn Error>> {
    let out_dir = PathBuf::from(env::var("OUT_DIR").unwrap());

    tonic_build::configure()
        .file_descriptor_set_path(out_dir.join("account_descriptor.bin"))
        .compile(&["proto/account.proto"], &["proto"])?;

    tonic_build::compile_protos("proto/account.proto")?;

    tonic_build::configure()
        .file_descriptor_set_path(out_dir.join("data_descriptor.bin"))
        .compile(&["proto/data.proto"], &["proto"])?;

    tonic_build::compile_protos("proto/data.proto")?;

    tonic_build::configure()
        .file_descriptor_set_path(out_dir.join("player_pos_descriptor.bin"))
        .compile(&["proto/player_pos.proto"], &["proto"])?;

    tonic_build::compile_protos("proto/player_pos.proto")?;

    Ok(())
}
