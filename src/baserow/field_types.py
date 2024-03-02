
import dataclasses
import enum
import typing as t

from databind.core.settings import Union

from .types import TableField


class TimeFormat(enum.Enum):
  HOUR_12 = 12
  HOUR_24 = 24


class FormulaType(enum.Enum):
  invalid = 'invalid'
  text = 'text'
  char = 'char'
  button = 'button'
  link = 'link'
  date_interval = 'date_interval'
  duration = 'duration'
  date = 'date'
  boolean = 'boolean'
  number = 'number'
  single_select = 'single_select'
  multiple_select = 'multiple_select'
  single_file = 'single_file'


class DateFormat(enum.Enum):
  EU = 'EU'
  US = 'US'
  ISO = 'ISO'


class RatingStyle(enum.Enum):
  star = 'star'
  heart = 'heart'
  thumbs_up = 'thumps-up'
  flag = 'flag'
  smile = 'smile'


@dataclasses.dataclass
class SelectOption:
  id: int
  value: str
  color: str


@Union.register(TableField, 'email')
@dataclasses.dataclass
class EMailTableField(TableField):
  pass


@Union.register(TableField, 'formula')
@dataclasses.dataclass
class FormulaTableField(TableField):
  nullable: bool
  formula: str
  number_decimal_places: t.Optional[int]
  date_force_timezone: t.Optional[str]
  date_time_format: t.Optional[str]
  duration_format: t.Optional[str]
  array_formula_type: t.Optional[str]
  date_include_time: t.Optional[bool]
  date_show_tzinfo: t.Optional[bool]
  error: t.Optional[str]
  date_format: t.Optional[str]
  formula_type: t.Optional[str]


@Union.register(TableField, 'text')
@dataclasses.dataclass
class TextTableField(TableField):
  text_default: str


@Union.register(TableField, 'long_text')
@dataclasses.dataclass
class LongTextTableField(TableField):
  pass


@Union.register(TableField, 'number')
@dataclasses.dataclass
class NumberTableField(TableField):
  number_decimal_places: t.Optional[int]
  number_negative: t.Optional[bool]


@Union.register(TableField, 'phone_number')
@dataclasses.dataclass
class PhoneTableField(TableField):
  pass


@Union.register(TableField, 'rating')
@dataclasses.dataclass
class RatingTableField(TableField):
  max_value: t.Optional[int]
  color: t.Optional[str]
  style: t.Optional[RatingStyle]


@Union.register(TableField, 'single_select')
@dataclasses.dataclass
class SingleSelectTableField(TableField):
  select_options: t.List[SelectOption]


@Union.register(TableField, 'url')
@dataclasses.dataclass
class UrlTableField(TableField):
  pass


@Union.register(TableField, 'uuid')
@dataclasses.dataclass
class UUIDTableField(TableField):
  pass


@Union.register(TableField, 'link_row')
@dataclasses.dataclass
class LinkRowTableField(TableField):
  link_row_table: int
  link_row_related_field: int


@Union.register(TableField, 'boolean')
@dataclasses.dataclass
class BooleanTableField(TableField):
  pass


@Union.register(TableField, 'file')
@dataclasses.dataclass
class FileTableField(TableField):
  pass
