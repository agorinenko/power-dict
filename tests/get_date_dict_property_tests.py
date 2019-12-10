import unittest
from datetime import datetime, timezone, timedelta, date

from power_dict.errors import NoneParameterError
from power_dict.utils import DictUtils


class GetDateDictPropertyTests(unittest.TestCase):
    properties = {
        "property_1": '2018-11-23',
        "property_2": date(2018, 11, 23),
        "property_3": '23.11.2018',
        "property_1_none": None
    }

    def test_get_property(self):
        target = DictUtils.get_date_dict_property(self.properties, 'property_1')
        self.assertIsInstance(target, date)
        self.assertEqual(target, date(2018, 11, 23))

        target = DictUtils.get_date_dict_property(self.properties, 'property_2')
        self.assertIsInstance(target, date)
        self.assertEqual(target, date(2018, 11, 23))

        target = DictUtils.get_date_dict_property(self.properties, 'property_3', format="%d.%m.%Y")
        self.assertIsInstance(target, date)
        self.assertEqual(target, date(2018, 11, 23))

        target = DictUtils.get_date_dict_property(self.properties, 'property_1_none',
                                                  default_value='2018-12-20')
        self.assertIsInstance(target, date)
        self.assertEqual(target, date(2018, 12, 20))

        target = DictUtils.get_date_dict_property(self.properties, 'key_not_found')
        self.assertEqual(target, None)

    def test_get_required_property(self):
        target = DictUtils.get_required_date_dict_property(self.properties, 'property_1')
        self.assertIsInstance(target, date)
        self.assertEqual(target, date(2018, 11, 23))

        target = DictUtils.get_required_date_dict_property(self.properties, 'property_2')
        self.assertIsInstance(target, date)
        self.assertEqual(target, date(2018, 11, 23))

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_date_dict_property(self.properties, 'property_1_none',
                                                      required_error="Key property_1_none is None")

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_date_dict_property(self.properties, 'key_not_found')
