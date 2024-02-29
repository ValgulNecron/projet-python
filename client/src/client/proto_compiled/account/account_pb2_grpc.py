# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import client.src.client.proto_compiled.account.account_pb2 as account__pb2


class AccountStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateAccount = channel.unary_unary(
                '/account.Account/CreateAccount',
                request_serializer=account__pb2.CreateAccountRequest.SerializeToString,
                response_deserializer=account__pb2.CreateAccountResponse.FromString,
                )
        self.GetAccount = channel.unary_unary(
                '/account.Account/GetAccount',
                request_serializer=account__pb2.GetAccountRequest.SerializeToString,
                response_deserializer=account__pb2.GetAccountResponse.FromString,
                )
        self.UpdateAccount = channel.unary_unary(
                '/account.Account/UpdateAccount',
                request_serializer=account__pb2.UpdateAccountRequest.SerializeToString,
                response_deserializer=account__pb2.UpdateAccountResponse.FromString,
                )
        self.DeleteAccount = channel.unary_unary(
                '/account.Account/DeleteAccount',
                request_serializer=account__pb2.DeleteAccountRequest.SerializeToString,
                response_deserializer=account__pb2.DeleteAccountResponse.FromString,
                )
        self.Login = channel.unary_unary(
                '/account.Account/Login',
                request_serializer=account__pb2.LoginRequest.SerializeToString,
                response_deserializer=account__pb2.LoginResponse.FromString,
                )


class AccountServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccountServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAccount,
                    request_deserializer=account__pb2.CreateAccountRequest.FromString,
                    response_serializer=account__pb2.CreateAccountResponse.SerializeToString,
            ),
            'GetAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAccount,
                    request_deserializer=account__pb2.GetAccountRequest.FromString,
                    response_serializer=account__pb2.GetAccountResponse.SerializeToString,
            ),
            'UpdateAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAccount,
                    request_deserializer=account__pb2.UpdateAccountRequest.FromString,
                    response_serializer=account__pb2.UpdateAccountResponse.SerializeToString,
            ),
            'DeleteAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAccount,
                    request_deserializer=account__pb2.DeleteAccountRequest.FromString,
                    response_serializer=account__pb2.DeleteAccountResponse.SerializeToString,
            ),
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=account__pb2.LoginRequest.FromString,
                    response_serializer=account__pb2.LoginResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'account.Account', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Account(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.Account/CreateAccount',
            account__pb2.CreateAccountRequest.SerializeToString,
            account__pb2.CreateAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.Account/GetAccount',
            account__pb2.GetAccountRequest.SerializeToString,
            account__pb2.GetAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.Account/UpdateAccount',
            account__pb2.UpdateAccountRequest.SerializeToString,
            account__pb2.UpdateAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.Account/DeleteAccount',
            account__pb2.DeleteAccountRequest.SerializeToString,
            account__pb2.DeleteAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.Account/Login',
            account__pb2.LoginRequest.SerializeToString,
            account__pb2.LoginResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
