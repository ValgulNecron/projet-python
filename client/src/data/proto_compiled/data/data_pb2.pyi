from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUserDataRequest(_message.Message):
    __slots__ = ("user_id", "token")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    token: str
    def __init__(self, user_id: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class GetUserDataResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Item]
    def __init__(self, items: _Optional[_Iterable[_Union[Item, _Mapping]]] = ...) -> None: ...

class Item(_message.Message):
    __slots__ = ("id", "nom", "type", "force", "endurance", "intelligence", "vitalite", "mana", "rarete", "vitesse", "sprite", "slot")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOM_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    ENDURANCE_FIELD_NUMBER: _ClassVar[int]
    INTELLIGENCE_FIELD_NUMBER: _ClassVar[int]
    VITALITE_FIELD_NUMBER: _ClassVar[int]
    MANA_FIELD_NUMBER: _ClassVar[int]
    RARETE_FIELD_NUMBER: _ClassVar[int]
    VITESSE_FIELD_NUMBER: _ClassVar[int]
    SPRITE_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    id: str
    nom: str
    type: str
    force: int
    endurance: int
    intelligence: int
    vitalite: int
    mana: int
    rarete: str
    vitesse: float
    sprite: bytes
    slot: int
    def __init__(self, id: _Optional[str] = ..., nom: _Optional[str] = ..., type: _Optional[str] = ..., force: _Optional[int] = ..., endurance: _Optional[int] = ..., intelligence: _Optional[int] = ..., vitalite: _Optional[int] = ..., mana: _Optional[int] = ..., rarete: _Optional[str] = ..., vitesse: _Optional[float] = ..., sprite: _Optional[bytes] = ..., slot: _Optional[int] = ...) -> None: ...

class AddUserDataRequest(_message.Message):
    __slots__ = ("user_id", "token", "item")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    token: str
    item: Item
    def __init__(self, user_id: _Optional[str] = ..., token: _Optional[str] = ..., item: _Optional[_Union[Item, _Mapping]] = ...) -> None: ...

class AddUserDataResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class UpdateUserDataRequest(_message.Message):
    __slots__ = ("user_id", "token", "old_item", "new_item")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    OLD_ITEM_FIELD_NUMBER: _ClassVar[int]
    NEW_ITEM_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    token: str
    old_item: Item
    new_item: Item
    def __init__(self, user_id: _Optional[str] = ..., token: _Optional[str] = ..., old_item: _Optional[_Union[Item, _Mapping]] = ..., new_item: _Optional[_Union[Item, _Mapping]] = ...) -> None: ...

class UpdateUserDataResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class DeleteUserDataRequest(_message.Message):
    __slots__ = ("user_id", "token", "item")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    token: str
    item: Item
    def __init__(self, user_id: _Optional[str] = ..., token: _Optional[str] = ..., item: _Optional[_Union[Item, _Mapping]] = ...) -> None: ...

class DeleteUserDataResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class GetItemListRequest(_message.Message):
    __slots__ = ("user_id", "token")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    token: str
    def __init__(self, user_id: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class GetItemListResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Item]
    def __init__(self, items: _Optional[_Iterable[_Union[Item, _Mapping]]] = ...) -> None: ...

class GetItemRequest(_message.Message):
    __slots__ = ("item_id", "user_id", "token")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    user_id: str
    token: str
    def __init__(self, item_id: _Optional[str] = ..., user_id: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class GetItemResponse(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: Item
    def __init__(self, item: _Optional[_Union[Item, _Mapping]] = ...) -> None: ...

class GetMapDataRequest(_message.Message):
    __slots__ = ("user_id", "token")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    token: str
    def __init__(self, user_id: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class GetMapDataResponse(_message.Message):
    __slots__ = ("map_tmx", "terrain_atlas_tsx", "terrain_atlas_png")
    MAP_TMX_FIELD_NUMBER: _ClassVar[int]
    TERRAIN_ATLAS_TSX_FIELD_NUMBER: _ClassVar[int]
    TERRAIN_ATLAS_PNG_FIELD_NUMBER: _ClassVar[int]
    map_tmx: bytes
    terrain_atlas_tsx: bytes
    terrain_atlas_png: bytes
    def __init__(self, map_tmx: _Optional[bytes] = ..., terrain_atlas_tsx: _Optional[bytes] = ..., terrain_atlas_png: _Optional[bytes] = ...) -> None: ...
