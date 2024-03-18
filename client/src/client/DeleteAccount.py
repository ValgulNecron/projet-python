import grpc
from client.src.client.proto_compiled.account import account_pb2_grpc, account_pb2


class DeleteAccount:
    id = ""
    token = ""

    def __init__(self, id, token):
        self.id = id
        self.token = token
    def delete_account(self):
        with grpc.insecure_channel("141.145.209.36:3333") as channel:
            stub = account_pb2_grpc.AccountStub(channel)
            response = stub.DeleteAccount(account_pb2.DeleteAccountRequest(id=self.id,token=self.token))
        print("client received: " + str(response.deleted) + ' ' + response.id)