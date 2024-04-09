# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import client.src.entity.proto_compiled.entity.player_pos_pb2 as player__pos__pb2


class PlayerPosServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PlayerGetPos = channel.unary_unary(
            '/player_pos.PlayerPosService/PlayerGetPos',
            request_serializer=player__pos__pb2.GetPosRequest.SerializeToString,
            response_deserializer=player__pos__pb2.GetPosResponse.FromString,
        )
        self.PlayerUpdatePos = channel.unary_unary(
            '/player_pos.PlayerPosService/PlayerUpdatePos',
            request_serializer=player__pos__pb2.UpdatePosRequest.SerializeToString,
            response_deserializer=player__pos__pb2.UpdatePosResponse.FromString,
        )
        self.PlayerGetAllPos = channel.unary_unary(
            '/player_pos.PlayerPosService/PlayerGetAllPos',
            request_serializer=player__pos__pb2.GetAllPosRequest.SerializeToString,
            response_deserializer=player__pos__pb2.GetAllPosResponse.FromString,
        )


class PlayerPosServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PlayerGetPos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PlayerUpdatePos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PlayerGetAllPos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PlayerPosServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'PlayerGetPos': grpc.unary_unary_rpc_method_handler(
            servicer.PlayerGetPos,
            request_deserializer=player__pos__pb2.GetPosRequest.FromString,
            response_serializer=player__pos__pb2.GetPosResponse.SerializeToString,
        ),
        'PlayerUpdatePos': grpc.unary_unary_rpc_method_handler(
            servicer.PlayerUpdatePos,
            request_deserializer=player__pos__pb2.UpdatePosRequest.FromString,
            response_serializer=player__pos__pb2.UpdatePosResponse.SerializeToString,
        ),
        'PlayerGetAllPos': grpc.unary_unary_rpc_method_handler(
            servicer.PlayerGetAllPos,
            request_deserializer=player__pos__pb2.GetAllPosRequest.FromString,
            response_serializer=player__pos__pb2.GetAllPosResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'player_pos.PlayerPosService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class PlayerPosService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PlayerGetPos(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(request, target, '/player_pos.PlayerPosService/PlayerGetPos',
                                             player__pos__pb2.GetPosRequest.SerializeToString,
                                             player__pos__pb2.GetPosResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PlayerUpdatePos(request,
                        target,
                        options=(),
                        channel_credentials=None,
                        call_credentials=None,
                        insecure=False,
                        compression=None,
                        wait_for_ready=None,
                        timeout=None,
                        metadata=None):
        return grpc.experimental.unary_unary(request, target, '/player_pos.PlayerPosService/PlayerUpdatePos',
                                             player__pos__pb2.UpdatePosRequest.SerializeToString,
                                             player__pos__pb2.UpdatePosResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PlayerGetAllPos(request,
                        target,
                        options=(),
                        channel_credentials=None,
                        call_credentials=None,
                        insecure=False,
                        compression=None,
                        wait_for_ready=None,
                        timeout=None,
                        metadata=None):
        return grpc.experimental.unary_unary(request, target, '/player_pos.PlayerPosService/PlayerGetAllPos',
                                             player__pos__pb2.GetAllPosRequest.SerializeToString,
                                             player__pos__pb2.GetAllPosResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
