
import dataclasses
import datetime
import enum
import typing as t

from databind.core.settings import Union

T = t.TypeVar('T')


class Permissions(enum.Enum):
  MEMBER = enum.auto()
  ADMIN = enum.auto()


@dataclasses.dataclass
class User:
  id: int
  first_name: str
  username: str
  is_staff: bool
  language: str


@dataclasses.dataclass
class Group:
  id: int
  name: str

@dataclasses.dataclass
class Workspace:
  id: int
  name: str

@dataclasses.dataclass
class OrderedGroup(Group):
  order: int


@dataclasses.dataclass
class PermissionedOrderedGroup(OrderedGroup):
  permissions: Permissions


@dataclasses.dataclass
class Table:
  id: int
  name: str
  order: int
  database_id: int


@Union(style=Union.FLAT)
@dataclasses.dataclass
class TableField:
  id: int
  table_id: int
  name: str
  order: int
  read_only: bool
  primary: bool


@dataclasses.dataclass
class Application:
  id: int
  name: str
  order: int
  type: str
  workspace: Workspace
  tables: t.List[Table]
  group: t.Optional[Group] = None


@dataclasses.dataclass
class Page(t.Generic[T]):
  count: int
  previous: t.Optional[int]
  next: t.Optional[int]
  results: t.List[T]


@dataclasses.dataclass
class Thumbnail:
  url: str
  width: t.Optional[int]
  height: t.Optional[int]


@dataclasses.dataclass
class File:
  size: int
  mime_type: t.Optional[str]
  is_image: t.Optional[bool]
  image_width: t.Optional[int]
  image_height: t.Optional[int]
  uploaded_at: datetime.datetime
  url: str
  thumbnails: t.Optional[t.Dict[str, Thumbnail]]
  name: str
  original_name: str


from . import field_types
