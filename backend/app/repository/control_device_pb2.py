# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: control_device.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'control_device.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x63ontrol_device.proto\x12\x06\x64\x65vice\"!\n\x0e\x43ontrolRequest\x12\x0f\n\x07\x63ontrol\x18\x01 \x01(\t\"\xa2\x01\n\x0f\x43ontrolResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x35\n\x07metrics\x18\x02 \x01(\x0b\x32\x1f.device.ControlResponse.MetricsH\x00\x88\x01\x01\x1a;\n\x07Metrics\x12\x15\n\rvelocity_list\x18\x01 \x03(\x02\x12\x19\n\x11\x61\x63\x63\x65leration_list\x18\x02 \x03(\x02\x42\n\n\x08_metrics2M\n\rControlDevice\x12<\n\x07\x43ontrol\x12\x16.device.ControlRequest\x1a\x17.device.ControlResponse\"\x00\x42\x1e\n\x0eio.grpc.deviceB\x06\x64\x65viceP\x01\xa2\x02\x01\x44\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'control_device_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\016io.grpc.deviceB\006deviceP\001\242\002\001D'
  _globals['_CONTROLREQUEST']._serialized_start=32
  _globals['_CONTROLREQUEST']._serialized_end=65
  _globals['_CONTROLRESPONSE']._serialized_start=68
  _globals['_CONTROLRESPONSE']._serialized_end=230
  _globals['_CONTROLRESPONSE_METRICS']._serialized_start=159
  _globals['_CONTROLRESPONSE_METRICS']._serialized_end=218
  _globals['_CONTROLDEVICE']._serialized_start=232
  _globals['_CONTROLDEVICE']._serialized_end=309
# @@protoc_insertion_point(module_scope)
