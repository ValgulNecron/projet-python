FROM rust:slim-bookworm AS builder

WORKDIR /projet-python

RUN USER=root cargo new --bin server

RUN apt-get update && apt-get install -y --no-install-recommends \
    libssl-dev libsqlite3-dev \
    libpng-dev libjpeg-dev \
    ca-certificates pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /projet-python/server

COPY ./Cargo.toml ./Cargo.toml

RUN cargo build --release
RUN rm src/*.rs

COPY ./src ./src

RUN rm ./target/release/deps/kasuki*
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

COPY --from=builder /projet-python/server/target/release/kasuki/ /kasuki/

CMD ["./server"]