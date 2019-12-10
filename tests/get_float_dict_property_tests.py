import unittest

from power_dict.errors import NoneParameterError
from power_dict.utils import DictUtils


class GetFloatDictPropertyTests(unittest.TestCase):
    properties = {
        "property_1": "1.01",
        "property_2": 2.02,
        "error": "oops..",
        "property_1_none": None
    }

    def test_get_property(self):
        target = DictUtils.get_float_dict_property(self.properties, 'property_1')
        self.assertIsInstance(target, float)
        self.assertEqual(target, 1.01)

        target = DictUtils.get_float_dict_property(self.properties, 'property_2')
        self.assertIsInstance(target, float)
        self.assertEqual(target, 2.02)

        target = DictUtils.get_float_dict_property(self.properties, 'property_1_none', default_value=3.03)
        self.assertIsInstance(target, float)
        self.assertEqual(target, 3.03)

        target = DictUtils.get_float_dict_property(self.properties, 'key_not_found')
        self.assertEqual(target, None)

    def test_get_required_property(self):
        target = DictUtils.get_required_float_dict_property(self.properties, 'property_1')
        self.assertIsInstance(target, float)
        self.assertEqual(target, 1.01)

        target = DictUtils.get_required_float_dict_property(self.properties, 'property_2')
        self.assertIsInstance(target, float)
        self.assertEqual(target, 2.02)

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_float_dict_property(self.properties, 'property_1_none',
                                                       required_error="Key property_1_none is None")

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_float_dict_property(self.properties, 'key_not_found')
