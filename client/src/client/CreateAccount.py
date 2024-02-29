import grpc
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
        with grpc.insecure_channel("141.145.209.36:3333") as channel:
            stub = account_pb2_grpc.AccountStub(channel)
            response = stub.CreateAccount(account_pb2.CreateAccountRequest(email=self.email,password=self.password,username=self.username))
        print("client received: " + str(response.created) + ' ' + response.id)
