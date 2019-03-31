# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: checkpoint.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='checkpoint.proto',
    package='paddle_hub_finetune_checkpoint',
    syntax='proto3',
    serialized_options=_b('H\003'),
    serialized_pb=_b(
        '\n\x10\x63heckpoint.proto\x12\x1epaddle_hub_finetune_checkpoint\"R\n\nCheckPoint\x12\x15\n\rcurrent_epoch\x18\x01 \x01(\x03\x12\x13\n\x0bglobal_step\x18\x02 \x01(\x03\x12\x18\n\x10latest_model_dir\x18\x03 \x01(\tB\x02H\x03\x62\x06proto3'
    ))

_CHECKPOINT = _descriptor.Descriptor(
    name='CheckPoint',
    full_name='paddle_hub_finetune_checkpoint.CheckPoint',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='current_epoch',
            full_name='paddle_hub_finetune_checkpoint.CheckPoint.current_epoch',
            index=0,
            number=1,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='global_step',
            full_name='paddle_hub_finetune_checkpoint.CheckPoint.global_step',
            index=1,
            number=2,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='latest_model_dir',
            full_name=
            'paddle_hub_finetune_checkpoint.CheckPoint.latest_model_dir',
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=52,
    serialized_end=134,
)

DESCRIPTOR.message_types_by_name['CheckPoint'] = _CHECKPOINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CheckPoint = _reflection.GeneratedProtocolMessageType(
    'CheckPoint',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_CHECKPOINT,
        __module__='checkpoint_pb2'
        # @@protoc_insertion_point(class_scope:paddle_hub_finetune_checkpoint.CheckPoint)
    ))
_sym_db.RegisterMessage(CheckPoint)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
