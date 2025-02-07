# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import app.repository.control_device_pb2 as control__device__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in control_device_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ControlDeviceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Control = channel.unary_unary(
                '/device.ControlDevice/Control',
                request_serializer=control__device__pb2.ControlRequest.SerializeToString,
                response_deserializer=control__device__pb2.ControlResponse.FromString,
                _registered_method=True)


class ControlDeviceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Control(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ControlDeviceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Control': grpc.unary_unary_rpc_method_handler(
                    servicer.Control,
                    request_deserializer=control__device__pb2.ControlRequest.FromString,
                    response_serializer=control__device__pb2.ControlResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'device.ControlDevice', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('device.ControlDevice', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ControlDevice(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Control(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/device.ControlDevice/Control',
            control__device__pb2.ControlRequest.SerializeToString,
            control__device__pb2.ControlResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
