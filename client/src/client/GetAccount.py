import grpc

from client import Global
from client.src.client.proto_compiled.account import account_pb2_grpc, account_pb2


class GetAccount:
    id = ""
    token = ""

    def __init__(self, id, token):
        self.id = id
        self.token = token

    def get_account(self):
        with grpc.insecure_channel(Global.IP) as channel:
            stub = account_pb2_grpc.AccountStub(channel)
            response = stub.GetAccount(account_pb2.GetAccountRequest(id=self.id, token=self.token))
        return response
