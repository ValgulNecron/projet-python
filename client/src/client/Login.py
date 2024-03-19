import grpc
from client.src.client.proto_compiled.account import account_pb2_grpc, account_pb2

class Login:
    username = ""
    password = ""

    def __init__(self, email, password):
        self.username = email
        self.password = password

    def login(self):
        with grpc.insecure_channel("141.145.209.36:3333") as channel:
            stub = account_pb2_grpc.AccountStub(channel)
            response = stub.Login(account_pb2.LoginRequest(username=self.username,password=self.password))
        print(response)