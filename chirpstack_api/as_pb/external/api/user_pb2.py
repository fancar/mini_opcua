# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/as_pb/external/api/user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,chirpstack-api/as_pb/external/api/user.proto\x12\x03\x61pi\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x8d\x02\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x1f\n\x0bsession_ttl\x18\x03 \x01(\x05R\nsessionTTL\x12\x10\n\x08is_admin\x18\x04 \x01(\x08\x12\x11\n\tis_active\x18\x05 \x01(\x08\x12\r\n\x05\x65mail\x18\x06 \x01(\t\x12\x0c\n\x04note\x18\x07 \x01(\t\x12\x0c\n\x04name\x18\x08 \x01(\t\x12\x0f\n\x07surname\x18\t \x01(\t\x12\x0f\n\x07\x63ompany\x18\n \x01(\t\x12\x10\n\x08position\x18\x0b \x01(\t\x12\r\n\x05phone\x18\x0c \x01(\t\x12,\n\x08login_at\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\x0flogin_with_ldap\x18\x0e \x01(\x08\"\xdf\x02\n\x0cUserListItem\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x1f\n\x0bsession_ttl\x18\x03 \x01(\x05R\nsessionTTL\x12\x10\n\x08is_admin\x18\x04 \x01(\x08\x12\x11\n\tis_active\x18\x05 \x01(\x08\x12.\n\ncreated_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08login_at\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\n \x01(\t\x12\x0f\n\x07surname\x18\x0b \x01(\t\x12\x0f\n\x07\x63ompany\x18\x0c \x01(\t\x12\x10\n\x08position\x18\r \x01(\t\x12\r\n\x05phone\x18\x0e \x01(\t\x12\x0f\n\x07org_cnt\x18\x0f \x01(\x05\"\xc0\x01\n\x0fUserLogListItem\x12\n\n\x02id\x18\x01 \x01(\x03\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07user_id\x18\x03 \x01(\x03\x12\x11\n\tuser_name\x18\x04 \x01(\t\x12\r\n\x05\x65vent\x18\x05 \x01(\t\x12\x12\n\nstate_prev\x18\x06 \x01(\t\x12\x11\n\tstate_cur\x18\x07 \x01(\t\x12\x17\n\x0forganization_id\x18\x08 \x01(\x03\"\x80\x01\n\x10UserOrganization\x12\'\n\x0forganization_id\x18\x01 \x01(\x03R\x0eorganizationID\x12\x10\n\x08is_admin\x18\x02 \x01(\x08\x12\x17\n\x0fis_device_admin\x18\x03 \x01(\x08\x12\x18\n\x10is_gateway_admin\x18\x04 \x01(\x08\"l\n\x11\x43reateUserRequest\x12\x17\n\x04user\x18\x01 \x01(\x0b\x32\t.api.User\x12\x10\n\x08password\x18\x02 \x01(\t\x12,\n\rorganizations\x18\x03 \x03(\x0b\x32\x15.api.UserOrganization\" \n\x12\x43reateUserResponse\x12\n\n\x02id\x18\x01 \x01(\x03\"\x1c\n\x0eGetUserRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"\x8a\x01\n\x0fGetUserResponse\x12\x17\n\x04user\x18\x01 \x01(\x0b\x32\t.api.User\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\",\n\x11UpdateUserRequest\x12\x17\n\x04user\x18\x01 \x01(\x0b\x32\t.api.User\"\x1f\n\x11\x44\x65leteUserRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"`\n\x0fListUserRequest\x12\r\n\x05limit\x18\x01 \x01(\x03\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0f\n\x07orderBy\x18\x03 \x01(\t\x12\r\n\x05order\x18\x04 \x01(\t\x12\x0e\n\x06search\x18\x05 \x01(\t\"J\n\x10ListUserResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\x03\x12!\n\x06result\x18\x02 \x03(\x0b\x32\x11.api.UserListItem\"}\n\x13ListUserLogsRequest\x12\r\n\x05limit\x18\x01 \x01(\x03\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x17\n\x0forganization_id\x18\x03 \x01(\x03\x12\x0e\n\x06search\x18\x04 \x01(\t\x12\x0f\n\x07orderBy\x18\x05 \x01(\t\x12\r\n\x05order\x18\x06 \x01(\t\"Q\n\x14ListUserLogsResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\x03\x12$\n\x06result\x18\x02 \x03(\x0b\x32\x14.api.UserLogListItem\">\n\x19UpdateUserPasswordRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x10\n\x08password\x18\x02 \x01(\t2\xee\x04\n\x0bUserService\x12G\n\x04List\x12\x14.api.ListUserRequest\x1a\x15.api.ListUserResponse\"\x12\x82\xd3\xe4\x93\x02\x0c\x12\n/api/users\x12I\n\x03Get\x12\x13.api.GetUserRequest\x1a\x14.api.GetUserResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/api/users/{id}\x12P\n\x06\x43reate\x12\x16.api.CreateUserRequest\x1a\x17.api.CreateUserResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\"\n/api/users:\x01*\x12Y\n\x06Update\x12\x16.api.UpdateUserRequest\x1a\x16.google.protobuf.Empty\"\x1f\x82\xd3\xe4\x93\x02\x19\x1a\x14/api/users/{user.id}:\x01*\x12Q\n\x06\x44\x65lete\x12\x16.api.DeleteUserRequest\x1a\x16.google.protobuf.Empty\"\x17\x82\xd3\xe4\x93\x02\x11*\x0f/api/users/{id}\x12r\n\x0eUpdatePassword\x12\x1e.api.UpdateUserPasswordRequest\x1a\x16.google.protobuf.Empty\"(\x82\xd3\xe4\x93\x02\"\x1a\x1d/api/users/{user_id}/password:\x01*\x12W\n\x08ListLogs\x12\x18.api.ListUserLogsRequest\x1a\x19.api.ListUserLogsResponse\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/api/user-logsBi\n!io.chirpstack.api.as.external.apiB\tUserProtoP\x01Z7github.com/brocaar/chirpstack-api/go/v3/as/external/apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.as_pb.external.api.user_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!io.chirpstack.api.as.external.apiB\tUserProtoP\001Z7github.com/brocaar/chirpstack-api/go/v3/as/external/api'
  _USERSERVICE.methods_by_name['List']._options = None
  _USERSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\014\022\n/api/users'
  _USERSERVICE.methods_by_name['Get']._options = None
  _USERSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\021\022\017/api/users/{id}'
  _USERSERVICE.methods_by_name['Create']._options = None
  _USERSERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\017\"\n/api/users:\001*'
  _USERSERVICE.methods_by_name['Update']._options = None
  _USERSERVICE.methods_by_name['Update']._serialized_options = b'\202\323\344\223\002\031\032\024/api/users/{user.id}:\001*'
  _USERSERVICE.methods_by_name['Delete']._options = None
  _USERSERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002\021*\017/api/users/{id}'
  _USERSERVICE.methods_by_name['UpdatePassword']._options = None
  _USERSERVICE.methods_by_name['UpdatePassword']._serialized_options = b'\202\323\344\223\002\"\032\035/api/users/{user_id}/password:\001*'
  _USERSERVICE.methods_by_name['ListLogs']._options = None
  _USERSERVICE.methods_by_name['ListLogs']._serialized_options = b'\202\323\344\223\002\020\022\016/api/user-logs'
  _USER._serialized_start=146
  _USER._serialized_end=415
  _USERLISTITEM._serialized_start=418
  _USERLISTITEM._serialized_end=769
  _USERLOGLISTITEM._serialized_start=772
  _USERLOGLISTITEM._serialized_end=964
  _USERORGANIZATION._serialized_start=967
  _USERORGANIZATION._serialized_end=1095
  _CREATEUSERREQUEST._serialized_start=1097
  _CREATEUSERREQUEST._serialized_end=1205
  _CREATEUSERRESPONSE._serialized_start=1207
  _CREATEUSERRESPONSE._serialized_end=1239
  _GETUSERREQUEST._serialized_start=1241
  _GETUSERREQUEST._serialized_end=1269
  _GETUSERRESPONSE._serialized_start=1272
  _GETUSERRESPONSE._serialized_end=1410
  _UPDATEUSERREQUEST._serialized_start=1412
  _UPDATEUSERREQUEST._serialized_end=1456
  _DELETEUSERREQUEST._serialized_start=1458
  _DELETEUSERREQUEST._serialized_end=1489
  _LISTUSERREQUEST._serialized_start=1491
  _LISTUSERREQUEST._serialized_end=1587
  _LISTUSERRESPONSE._serialized_start=1589
  _LISTUSERRESPONSE._serialized_end=1663
  _LISTUSERLOGSREQUEST._serialized_start=1665
  _LISTUSERLOGSREQUEST._serialized_end=1790
  _LISTUSERLOGSRESPONSE._serialized_start=1792
  _LISTUSERLOGSRESPONSE._serialized_end=1873
  _UPDATEUSERPASSWORDREQUEST._serialized_start=1875
  _UPDATEUSERPASSWORDREQUEST._serialized_end=1937
  _USERSERVICE._serialized_start=1940
  _USERSERVICE._serialized_end=2562
# @@protoc_insertion_point(module_scope)