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
Get the dictionary value and cast it to type data_type. [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_value_tests.py)
## DictUtils.get_required_value(properties: dict, key: str, **kwargs) -> object
Get the required dictionary value and cast it to type data_type. [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_required_value_tests.py)
## DictUtils.get_setting_by_path(properties: dict, path: str, **kwargs) -> object
Get the dictionary value and cast it to type data_type by path. [See tests for examples.](https://github.com/agorinenko/power-dict/blob/master/tests/get_setting_by_path_tests.py)
