# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: simple_waymo_open_dataset_reader/label.proto
# Protobuf Python Version: 5.29.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    3,
    '',
    'simple_waymo_open_dataset_reader/label.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,simple_waymo_open_dataset_reader/label.proto\x12\x12waymo.open_dataset\"\xee\x05\n\x05Label\x12*\n\x03\x62ox\x18\x01 \x01(\x0b\x32\x1d.waymo.open_dataset.Label.Box\x12\x34\n\x08metadata\x18\x02 \x01(\x0b\x32\".waymo.open_dataset.Label.Metadata\x12,\n\x04type\x18\x03 \x01(\x0e\x32\x1e.waymo.open_dataset.Label.Type\x12\n\n\x02id\x18\x04 \x01(\t\x12M\n\x1a\x64\x65tection_difficulty_level\x18\x05 \x01(\x0e\x32).waymo.open_dataset.Label.DifficultyLevel\x12L\n\x19tracking_difficulty_level\x18\x06 \x01(\x0e\x32).waymo.open_dataset.Label.DifficultyLevel\x1a\xbf\x01\n\x03\x42ox\x12\x10\n\x08\x63\x65nter_x\x18\x01 \x01(\x01\x12\x10\n\x08\x63\x65nter_y\x18\x02 \x01(\x01\x12\x10\n\x08\x63\x65nter_z\x18\x03 \x01(\x01\x12\x0e\n\x06length\x18\x05 \x01(\x01\x12\r\n\x05width\x18\x04 \x01(\x01\x12\x0e\n\x06height\x18\x06 \x01(\x01\x12\x0f\n\x07heading\x18\x07 \x01(\x01\"B\n\x04Type\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\x0b\n\x07TYPE_3D\x10\x01\x12\x0b\n\x07TYPE_2D\x10\x02\x12\x0e\n\nTYPE_AA_2D\x10\x03\x1aN\n\x08Metadata\x12\x0f\n\x07speed_x\x18\x01 \x01(\x01\x12\x0f\n\x07speed_y\x18\x02 \x01(\x01\x12\x0f\n\x07\x61\x63\x63\x65l_x\x18\x03 \x01(\x01\x12\x0f\n\x07\x61\x63\x63\x65l_y\x18\x04 \x01(\x01\"`\n\x04Type\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\x10\n\x0cTYPE_VEHICLE\x10\x01\x12\x13\n\x0fTYPE_PEDESTRIAN\x10\x02\x12\r\n\tTYPE_SIGN\x10\x03\x12\x10\n\x0cTYPE_CYCLIST\x10\x04\"8\n\x0f\x44ifficultyLevel\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07LEVEL_1\x10\x01\x12\x0b\n\x07LEVEL_2\x10\x02\"2\n\x0ePolygon2dProto\x12\t\n\x01x\x18\x01 \x03(\x01\x12\t\n\x01y\x18\x02 \x03(\x01\x12\n\n\x02id\x18\x03 \x01(\t')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'simple_waymo_open_dataset_reader.label_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_LABEL']._serialized_start=69
  _globals['_LABEL']._serialized_end=819
  _globals['_LABEL_BOX']._serialized_start=392
  _globals['_LABEL_BOX']._serialized_end=583
  _globals['_LABEL_BOX_TYPE']._serialized_start=517
  _globals['_LABEL_BOX_TYPE']._serialized_end=583
  _globals['_LABEL_METADATA']._serialized_start=585
  _globals['_LABEL_METADATA']._serialized_end=663
  _globals['_LABEL_TYPE']._serialized_start=665
  _globals['_LABEL_TYPE']._serialized_end=761
  _globals['_LABEL_DIFFICULTYLEVEL']._serialized_start=763
  _globals['_LABEL_DIFFICULTYLEVEL']._serialized_end=819
  _globals['_POLYGON2DPROTO']._serialized_start=821
  _globals['_POLYGON2DPROTO']._serialized_end=871
# @@protoc_insertion_point(module_scope)
