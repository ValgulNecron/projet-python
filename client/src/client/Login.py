from tkinter import messagebox

import grpc

from client import Global
from client.src.client.proto_compiled.account import account_pb2_grpc, account_pb2


class Login:
    username = ""
    password = ""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        with grpc.insecure_channel(Global.IP) as channel:
            stub = account_pb2_grpc.AccountStub(channel)
            response = stub.Login(account_pb2.LoginRequest(username=self.username, password=self.password))
        if response.token == "":
            messagebox.showerror("Error", "Invalid username or password")
            return
        Global.ID = response.id
        Global.TOKEN = response.token
