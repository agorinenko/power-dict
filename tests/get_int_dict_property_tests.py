import unittest

from power_dict.errors import NoneParameterError
from power_dict.utils import DictUtils


class GetIntDictPropertyTests(unittest.TestCase):
    properties = {
        "property_1": "1",
        "property_2": 2,
        "property_1_none": None
    }

    def test_get_property(self):
        target = DictUtils.get_int_dict_property(self.properties, 'property_1')
        self.assertIsInstance(target, int)
        self.assertEqual(target, 1)

        target = DictUtils.get_int_dict_property(self.properties, 'property_2')
        self.assertIsInstance(target, int)
        self.assertEqual(target, 2)

        target = DictUtils.get_int_dict_property(self.properties, 'property_1_none', default_value=3)
        self.assertIsInstance(target, int)
        self.assertEqual(target, 3)

        target = DictUtils.get_int_dict_property(self.properties, 'key_not_found')
        self.assertEqual(target, None)

    def test_get_required_property(self):
        target = DictUtils.get_int_dict_property(self.properties, 'property_1')
        self.assertIsInstance(target, int)
        self.assertEqual(target, 1)

        target = DictUtils.get_int_dict_property(self.properties, 'property_2')
        self.assertIsInstance(target, int)
        self.assertEqual(target, 2)

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_str_dict_property(self.properties, 'property_1_none',
                                                     required_error="Key property_1_none is None")

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_str_dict_property(self.properties, 'key_not_found')
