import grpc
from client.src.client.proto_compiled.account import account_pb2_grpc, account_pb2

class UpdateAccount:
    id = ""
    token = ""
    email = ""
    password = ""
    username = ""

    def __init__(self, id, token, email, password, username):
        self.id = id
        self.token = token
        self.email = email
        self.password = password
        self.username = username
    def update_account(self):
        with grpc.insecure_channel("141.145.209.36:3333") as channel:
            stub = account_pb2_grpc.AccountStub(channel)
            response = stub.UpdateAccount(account_pb2.UpdateAccountRequest(id=self.id,token=self.token,email=self.email,password=self.password,username=self.username))
        print("client received: " + str(response.updated) + ' ' + response.id)