# What's the good of that?
[![PyPI version](https://badge.fury.io/py/power-dict.svg)](https://pypi.org/project/power-dict/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/power-dict)](https://img.shields.io/pypi/pyversions/power-dict)
[![License](https://img.shields.io/pypi/l/power-dict)](https://img.shields.io/pypi/l/power-dict)
1. Get the dictionary value and cast it to data type 
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
