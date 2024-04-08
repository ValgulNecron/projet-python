from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PosWrapper(_message.Message):
    __slots__ = ("user_id", "pos")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    pos: Pos
    def __init__(self, user_id: _Optional[str] = ..., pos: _Optional[_Union[Pos, _Mapping]] = ...) -> None: ...

class Pos(_message.Message):
    __slots__ = ("pos_x", "pos_y", "last_update")
    POS_X_FIELD_NUMBER: _ClassVar[int]
    POS_Y_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_FIELD_NUMBER: _ClassVar[int]
    pos_x: int
    pos_y: int
    last_update: int
    def __init__(self, pos_x: _Optional[int] = ..., pos_y: _Optional[int] = ..., last_update: _Optional[int] = ...) -> None: ...

class GetPosRequest(_message.Message):
    __slots__ = ("user_id", "token")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    token: str
    def __init__(self, user_id: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class GetPosResponse(_message.Message):
    __slots__ = ("user_id", "pos")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    pos: Pos
    def __init__(self, user_id: _Optional[str] = ..., pos: _Optional[_Union[Pos, _Mapping]] = ...) -> None: ...

class UpdatePosRequest(_message.Message):
    __slots__ = ("user_id", "token", "pos")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    token: str
    pos: Pos
    def __init__(self, user_id: _Optional[str] = ..., token: _Optional[str] = ..., pos: _Optional[_Union[Pos, _Mapping]] = ...) -> None: ...

class UpdatePosResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class GetAllPosRequest(_message.Message):
    __slots__ = ("user_id", "token")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    token: str
    def __init__(self, user_id: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class GetAllPosResponse(_message.Message):
    __slots__ = ("pos",)
    POS_FIELD_NUMBER: _ClassVar[int]
    pos: _containers.RepeatedCompositeFieldContainer[PosWrapper]
    def __init__(self, pos: _Optional[_Iterable[_Union[PosWrapper, _Mapping]]] = ...) -> None: ...
