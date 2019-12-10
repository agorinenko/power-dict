import unittest
from datetime import datetime, timezone, timedelta

from power_dict.errors import NoneParameterError, InvalidParameterError
from power_dict.utils import DictUtils


class GetDateTimeDictPropertyTests(unittest.TestCase):
    properties = {
        "property_1": '2018-11-23 01:45:59',
        "property_2": datetime(2018, 11, 23, 1, 45, 59),
        "property_3": '23.11.2018T01:45:59+0300',
        "error": "oops..",
        "property_1_none": None
    }

    def test_get_property(self):
        target = DictUtils.get_datetime_dict_property(self.properties, 'property_1')
        self.assertIsInstance(target, datetime)
        self.assertEqual(target, datetime(2018, 11, 23, 1, 45, 59))

        target = DictUtils.get_datetime_dict_property(self.properties, 'property_2')
        self.assertIsInstance(target, datetime)
        self.assertEqual(target, datetime(2018, 11, 23, 1, 45, 59))

        target = DictUtils.get_datetime_dict_property(self.properties, 'property_3', format="%d.%m.%YT%H:%M:%S%z")
        self.assertIsInstance(target, datetime)
        self.assertEqual(target, datetime(2018, 11, 23, 1, 45, 59, tzinfo=timezone(timedelta(hours=3))))

        target = DictUtils.get_datetime_dict_property(self.properties, 'property_1_none',
                                                      default_value='2018-12-20 01:45:59')
        self.assertIsInstance(target, datetime)
        self.assertEqual(target, datetime(2018, 12, 20, 1, 45, 59))

        target = DictUtils.get_datetime_dict_property(self.properties, 'key_not_found')
        self.assertEqual(target, None)

        with self.assertRaises(InvalidParameterError):
            DictUtils.get_datetime_dict_property(self.properties, 'error')

    def test_get_required_property(self):
        target = DictUtils.get_required_datetime_dict_property(self.properties, 'property_1')
        self.assertIsInstance(target, datetime)
        self.assertEqual(target, datetime(2018, 11, 23, 1, 45, 59))

        target = DictUtils.get_required_datetime_dict_property(self.properties, 'property_2')
        self.assertIsInstance(target, datetime)
        self.assertEqual(target, datetime(2018, 11, 23, 1, 45, 59))

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_datetime_dict_property(self.properties, 'property_1_none',
                                                          required_error="Key property_1_none is None")

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_datetime_dict_property(self.properties, 'key_not_found')

        with self.assertRaises(InvalidParameterError):
            DictUtils.get_required_datetime_dict_property(self.properties, 'error')
