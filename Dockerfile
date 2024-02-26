FROM rust:slim-bookworm AS builder

RUN USER=root cargo new --bin server

RUN apt-get update && apt-get install -y --no-install-recommends \
    libssl-dev libsqlite3-dev \
    libpng-dev libjpeg-dev \
    ca-certificates pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /server

COPY ./server/Cargo.toml ./Cargo.toml

RUN cargo build --release
RUN rm src/*.rs
COPY ./server/proto ./proto

COPY ./server/src ./src

RUN rm ./target/release/deps/server*
RUN cargo build --release

FROM debian:trixie-slim AS server

LABEL maintainer="valgul"
LABEL author="valgul"

WORKDIR /server/

RUN apt-get update && apt-get install -y --no-install-recommends \
    libssl-dev libsqlite3-dev \
    libpng-dev libjpeg-dev \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /server/target/release/server/ /server/

CMD ["./server"]