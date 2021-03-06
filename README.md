# What's the good of that?
[![PyPI version](https://badge.fury.io/py/power-dict.svg)](https://pypi.org/project/power-dict/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/power-dict)](https://img.shields.io/pypi/pyversions/power-dict)
[![License](https://img.shields.io/pypi/l/power-dict)](https://img.shields.io/pypi/l/power-dict)
1. Validate and transform an incoming dictionary based on schema rules
1. Get the dictionary value and cast string representation to target data type 
1. Available types:

"object": raw object

"str": textual data

"int": integer numeric type

"float": float numeric type

"decimal": decimal numeric type

"list": list sequence type

"datetime": a datetime object is a single object containing all the information from a date object and a time object

"date": a date object represents a date (year, month and day)

"bool": boolean values are the two constant objects False and True
1. Set default value if result is None
1. Get the required dictionary value and cast it to data type
1. Get the required dictionary value and raise error if value is empty
## install
```
pip install power-dict
```
## import
``` python
from power_dict.utils import DictUtils
```
## Run unittest from console
```
python -m unittest discover -p "*_tests.py"
```
## SchemaValidator.validate(context: dict, schema: list, sanitize_schema: bool = True) -> dict
Validation and transformation of 'context' dictionary in accordance with the rules of the scheme. [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/schema_validator_tests.py)
## DictUtils.get_value(properties: dict, key: str, **kwargs) -> object
Get the dictionary value and cast it to object. [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_value_tests.py)
## DictUtils.get_required_value(properties: dict, key: str, **kwargs) -> object
Get the required dictionary value and cast it to object. [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_required_value_tests.py)
## DictUtils.get_setting_by_path(properties: dict, path: str, **kwargs) -> object
Get the dictionary value and cast it to object by path. [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_setting_by_path_tests.py)
## DictUtils.get_dict_property(properties: dict, key: str, default_value=None) -> object
Get the dictionary value. [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_dict_property_tests.py)
## DictUtils.get_required_dict_property(properties: dict, key: str, required_error=None) -> object
Get the required dictionary value. [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_dict_property_tests.py)
## DictUtils.get_str_dict_property(properties: dict, key: str, default_value='') -> str
Get the dictionary value and cast it to 'str'. [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_str_dict_property_tests.py)
## DictUtils.get_required_str_dict_property(properties: dict, key: str, required_error=None) -> str
Get the required dictionary value and cast it to 'str'. [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_str_dict_property_tests.py)
## DictUtils.get_int_dict_property(properties: dict, key: str, default_value=None) -> int
Get the dictionary value and cast it to 'int'. [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_int_dict_property_tests.py)
## DictUtils.get_required_int_dict_property(properties: dict, key: str, required_error=None) -> int
Get the required dictionary value and cast it to 'int'. [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_int_dict_property_tests.py)
## DictUtils.get_datetime_dict_property(properties: dict, key: str, default_value: datetime = None, format: str = None) -> datetime
 Get the dictionary value and cast it to 'datetime'. 
 [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_datetime_dict_property_tests.py)
 [Format Codes.](https://docs.python.org/3.8/library/datetime.html#strftime-and-strptime-format-codes)
## DictUtils.get_required_datetime_dict_property(properties: dict, key: str, required_error=None, format: str = None) -> datetime
Get the required dictionary value and cast it to 'datetime'. 
[See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_datetime_dict_property_tests.py)
[Format Codes.](https://docs.python.org/3.8/library/datetime.html#strftime-and-strptime-format-codes)
## DictUtils.get_date_dict_property(properties: dict, key: str, default_value=None, format: str = None) -> datetime.date
Get the dictionary value and cast it to 'date'.
 [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_date_dict_property_tests.py)
 [Format Codes.](https://docs.python.org/3.8/library/datetime.html#strftime-and-strptime-format-codes)
## DictUtils.get_required_date_dict_property(properties: dict, key: str, required_error=None, format: str = None) -> datetime.date
Get the required dictionary value and cast it to 'date'.
[See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_date_dict_property_tests.py)
[Format Codes.](https://docs.python.org/3.8/library/datetime.html#strftime-and-strptime-format-codes)
## DictUtils.get_bool_dict_property(properties: dict, key: str, default_value=None) -> bool
Get the dictionary value and cast it to 'bool'. [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_bool_dict_property_tests.py)
## DictUtils.get_required_bool_dict_property(properties: dict, key: str, required_error=None) -> bool
Get the required dictionary value and cast it to 'bool'. [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_bool_dict_property_tests.py)
## DictUtils.get_decimal_dict_property(properties: dict, key: str, default_value=None) -> Decimal
Get the dictionary value and cast it to 'decimal'. [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_decimal_dict_property_tests.py)
## DictUtils.get_required_decimal_dict_property(properties: dict, key: str, required_error=None) -> Decimal
Get the required dictionary value and cast it to 'decimal'. [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_decimal_dict_property_tests.py)
## DictUtils.get_list_dict_property(properties: dict, key: str, default_value=None) -> list
Get the dictionary value and cast it to 'list'. [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_list_dict_property_tests.py)
## DictUtils.get_required_list_dict_property(properties: dict, key: str, required_error=None) -> list
Get the required dictionary value and cast it to 'list'. [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_list_dict_property_tests.py)
## DictUtils.get_float_dict_property(properties: dict, key: str, default_value=None) -> float
Get the dictionary value and cast it to 'float'. [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_float_dict_property_tests.py)
## DictUtils.get_required_float_dict_property(properties: dict, key: str, required_error=None) -> float
Get the required dictionary value and cast it to 'float'. [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_float_dict_property_tests.py)
