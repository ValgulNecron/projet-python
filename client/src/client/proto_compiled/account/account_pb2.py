# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/account.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13proto/account.proto\x12\x07\x61\x63\x63ount\"I\n\x14\x43reateAccountRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\"4\n\x15\x43reateAccountResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x63reated\x18\x02 \x01(\x08\".\n\x11GetAccountRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\"c\n\x12GetAccountResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x0f\n\x07\x63reated\x18\x04 \x01(\t\x12\x0f\n\x07updated\x18\x05 \x01(\t\"d\n\x14UpdateAccountRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x10\n\x08username\x18\x05 \x01(\t\"4\n\x15UpdateAccountResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07updated\x18\x02 \x01(\x08\"1\n\x14\x44\x65leteAccountRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\"4\n\x15\x44\x65leteAccountResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x65leted\x18\x02 \x01(\x08\"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\":\n\rLoginResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06logged\x18\x02 \x01(\x08\x12\r\n\x05token\x18\x03 \x01(\t2\xf8\x02\n\x07\x41\x63\x63ount\x12N\n\rCreateAccount\x12\x1d.account.CreateAccountRequest\x1a\x1e.account.CreateAccountResponse\x12\x45\n\nGetAccount\x12\x1a.account.GetAccountRequest\x1a\x1b.account.GetAccountResponse\x12N\n\rUpdateAccount\x12\x1d.account.UpdateAccountRequest\x1a\x1e.account.UpdateAccountResponse\x12N\n\rDeleteAccount\x12\x1d.account.DeleteAccountRequest\x1a\x1e.account.DeleteAccountResponse\x12\x36\n\x05Login\x12\x15.account.LoginRequest\x1a\x16.account.LoginResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.account_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CREATEACCOUNTREQUEST']._serialized_start=32
  _globals['_CREATEACCOUNTREQUEST']._serialized_end=105
  _globals['_CREATEACCOUNTRESPONSE']._serialized_start=107
  _globals['_CREATEACCOUNTRESPONSE']._serialized_end=159
  _globals['_GETACCOUNTREQUEST']._serialized_start=161
  _globals['_GETACCOUNTREQUEST']._serialized_end=207
  _globals['_GETACCOUNTRESPONSE']._serialized_start=209
  _globals['_GETACCOUNTRESPONSE']._serialized_end=308
  _globals['_UPDATEACCOUNTREQUEST']._serialized_start=310
  _globals['_UPDATEACCOUNTREQUEST']._serialized_end=410
  _globals['_UPDATEACCOUNTRESPONSE']._serialized_start=412
  _globals['_UPDATEACCOUNTRESPONSE']._serialized_end=464
  _globals['_DELETEACCOUNTREQUEST']._serialized_start=466
  _globals['_DELETEACCOUNTREQUEST']._serialized_end=515
  _globals['_DELETEACCOUNTRESPONSE']._serialized_start=517
  _globals['_DELETEACCOUNTRESPONSE']._serialized_end=569
  _globals['_LOGINREQUEST']._serialized_start=571
  _globals['_LOGINREQUEST']._serialized_end=621
  _globals['_LOGINRESPONSE']._serialized_start=623
  _globals['_LOGINRESPONSE']._serialized_end=681
  _globals['_ACCOUNT']._serialized_start=684
  _globals['_ACCOUNT']._serialized_end=1060
# @@protoc_insertion_point(module_scope)
