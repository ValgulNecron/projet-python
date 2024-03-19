from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAccountRequest(_message.Message):
    __slots__ = ("email", "password", "username")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    username: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...

class CreateAccountResponse(_message.Message):
    __slots__ = ("id", "created")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    id: str
    created: bool
    def __init__(self, id: _Optional[str] = ..., created: bool = ...) -> None: ...

class GetAccountRequest(_message.Message):
    __slots__ = ("id", "token")
    ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    token: str
    def __init__(self, id: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class GetAccountResponse(_message.Message):
    __slots__ = ("id", "email", "username", "created", "updated")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    id: str
    email: str
    username: str
    created: str
    updated: str
    def __init__(self, id: _Optional[str] = ..., email: _Optional[str] = ..., username: _Optional[str] = ..., created: _Optional[str] = ..., updated: _Optional[str] = ...) -> None: ...

class UpdateAccountRequest(_message.Message):
    __slots__ = ("id", "token", "email", "password", "username")
    ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    token: str
    email: str
    password: str
    username: str
    def __init__(self, id: _Optional[str] = ..., token: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...

class UpdateAccountResponse(_message.Message):
    __slots__ = ("id", "updated")
    ID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    id: str
    updated: bool
    def __init__(self, id: _Optional[str] = ..., updated: bool = ...) -> None: ...

class DeleteAccountRequest(_message.Message):
    __slots__ = ("id", "token")
    ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    token: str
    def __init__(self, id: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class DeleteAccountResponse(_message.Message):
    __slots__ = ("id", "deleted")
    ID_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    id: str
    deleted: bool
    def __init__(self, id: _Optional[str] = ..., deleted: bool = ...) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ("id", "logged", "token")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOGGED_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    logged: bool
    token: str
    def __init__(self, id: _Optional[str] = ..., logged: bool = ..., token: _Optional[str] = ...) -> None: ...
