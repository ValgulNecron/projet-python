def make_request(payload, endpoint):
    grpc = HTTPX.plugin("grpc")
    client = grpc.Client("http://141.145.209.36:3333")
    response = client.post(endpoint, json=payload)
    return response.json()
