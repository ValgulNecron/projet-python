import grpc

from client import Global
from client.src.client.proto_compiled.account import account_pb2_grpc, account_pb2


class CreateAccount:
    email = ""
    password = ""
    username = ""

    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username

    def create_account(self):
        with grpc.insecure_channel(Global.IP) as channel:
            stub = account_pb2_grpc.AccountStub(channel)
            response = stub.CreateAccount(
                account_pb2.CreateAccountRequest(email=self.email, password=self.password, username=self.username))
        print(response)
        Global.ID = response.id
        print(Global.ID)
