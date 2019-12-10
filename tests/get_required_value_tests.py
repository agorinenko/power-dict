import unittest

from datetime import date, datetime
from decimal import Decimal
from power_dict.errors import NoneParameterError
from power_dict.utils import DictUtils


class GetRequiredValueTests(unittest.TestCase):
    properties = {
        "object": {
            "object_1": 1
        },
        "object_none": None,
        "str": "Hello!",
        "str_none": None,
        "int": "1",
        "int_none": None,
        "datetime": '2018-11-23 01:45:59',
        "datetime_none": None,
        "datetime.date": '23.11.2018',
        "datetime.date_none": None,
        "bool": 'true',
        "bool_none": None,
        "decimal": "1.01",
        "decimal_none": None,
        "list": [1, 2, 3],
        "list_none": None,
        "float": '2.02',
        "float_none": None
    }

    def test_get_required_value(self):
        target = DictUtils.get_required_value(self.properties, 'object', data_type='object')
        self.assertIsInstance(target, object)
        self.assertEqual(target, {"object_1": 1})

        target = DictUtils.get_required_value(self.properties, 'str', data_type="str")
        self.assertIsInstance(target, str)
        self.assertEqual(target, "Hello!")

        target = DictUtils.get_required_value(self.properties, 'int', data_type="int")
        self.assertIsInstance(target, int)
        self.assertEqual(target, 1)

        target = DictUtils.get_required_value(self.properties, 'datetime', data_type="datetime")
        self.assertIsInstance(target, datetime)
        self.assertEqual(target, datetime(2018, 11, 23, 1, 45, 59))

        target = DictUtils.get_required_value(self.properties, 'datetime.date', data_type="date", format='%d.%m.%Y')
        self.assertIsInstance(target, date)
        self.assertEqual(target, date(2018, 11, 23))

        target = DictUtils.get_required_value(self.properties, 'bool', data_type="bool")
        self.assertIsInstance(target, bool)
        self.assertEqual(target, True)

        target = DictUtils.get_required_value(self.properties, 'decimal', data_type="decimal")
        self.assertIsInstance(target, Decimal)
        self.assertEqual(target, Decimal('1.01'))

        target = DictUtils.get_required_value(self.properties, 'list', data_type="list")
        self.assertIsInstance(target, list)
        self.assertEqual(target, [1, 2, 3])

        target = DictUtils.get_required_value(self.properties, 'float', data_type="float")
        self.assertIsInstance(target, float)
        self.assertEqual(target, 2.02)

    def test_get_required_value_error(self):
        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_value(self.properties, 'object_none2')

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_value(self.properties, 'object_none', data_type="object")

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_value(self.properties, 'str_none', data_type="str")

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_value(self.properties, 'int_none', data_type="int")

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_value(self.properties, 'datetime_none', data_type="datetime")

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_value(self.properties, 'datetime.date_none', data_type="date", format='%d.%m.%Y')

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_value(self.properties, 'bool_none', data_type="bool")

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_value(self.properties, 'decimal_none', data_type="decimal")

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_value(self.properties, 'list_none', data_type="list")

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_value(self.properties, 'float_none', data_type="float")
