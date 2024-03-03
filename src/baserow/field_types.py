
import dataclasses
import enum
import typing as t

from databind.core.settings import Union

from .types import TableField


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


@Union.register(TableField, 'date')
@Union.register(TableField, 'last_modified')
@Union.register(TableField, 'created_on')
@dataclasses.dataclass
class DateTableField(TableField):
  date_format: t.Optional[DateFormat]
  date_include_time: t.Optional[bool]
  date_time_format: t.Optional[str]
  date_show_tzinfo: t.Optional[bool]
  date_force_timezone: t.Optional[str]


@Union.register(TableField, 'duration')
@dataclasses.dataclass
class DurationTableField(TableField):
  duration_format: t.Optional[str]


@Union.register(TableField, 'email')
@dataclasses.dataclass
class EMailTableField(TableField):
  pass


@Union.register(TableField, 'count')
@dataclasses.dataclass
class CountTableField(TableField):
  nullable: bool
  number_decimal_places: t.Optional[int]
  date_force_timezone: t.Optional[str]
  date_time_format: t.Optional[str]
  duration_format: t.Optional[str]
  array_formula_type: t.Optional[str]
  date_include_time: t.Optional[bool]
  date_show_tzinfo: t.Optional[bool]
  error: t.Optional[str]
  date_format: t.Optional[str]
  through_field_id: t.Optional[int]
  formula_type: t.Optional[str]


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


@Union.register(TableField, 'lookup')
@dataclasses.dataclass
class LookupTableField(TableField):
  nullable: bool
  number_decimal_places: t.Optional[int]
  date_force_timezone: t.Optional[str]
  date_time_format: t.Optional[str]
  duration_format: t.Optional[str]
  array_formula_type: t.Optional[str]
  date_include_time: t.Optional[bool]
  date_show_tzinfo: t.Optional[bool]
  error: t.Optional[str]
  date_format: t.Optional[str]
  through_field_id: t.Optional[int]
  through_field_name: t.Optional[str]
  target_field_id: t.Optional[int]
  target_field_name: t.Optional[str]
  rollup_function: t.Optional[str]
  formula_type: t.Optional[str]


@Union.register(TableField, 'text')
@dataclasses.dataclass
class TextTableField(TableField):
  text_default: str


@Union.register(TableField, 'created_by')
@Union.register(TableField, 'last_modified_by')
@dataclasses.dataclass
class UserTableField(TableField):
  pass

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


@Union.register(TableField, 'rollup')
@dataclasses.dataclass
class RollupTableField(TableField):
  nullable: bool
  number_decimal_places: t.Optional[int]
  date_force_timezone: t.Optional[str]
  date_time_format: t.Optional[str]
  duration_format: t.Optional[str]
  array_formula_type: t.Optional[str]
  date_include_time: t.Optional[bool]
  date_show_tzinfo: t.Optional[bool]
  error: t.Optional[str]
  date_format: t.Optional[str]
  through_field_id: t.Optional[int]
  target_field_id: t.Optional[int]
  rollup_function: t.Optional[str]
  formula_type: t.Optional[str]


@Union.register(TableField, 'single_select')
@Union.register(TableField, 'multiple_select')
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
  link_row_table_id: t.Optional[int]
  link_row_related_field_id: t.Optional[int]
  # Deprecated
  link_row_table: t.Optional[int]
  # Deprecated
  link_row_related_field: t.Optional[int]


@Union.register(TableField, 'boolean')
@dataclasses.dataclass
class BooleanTableField(TableField):
  pass


@Union.register(TableField, 'file')
@dataclasses.dataclass
class FileTableField(TableField):
  pass
