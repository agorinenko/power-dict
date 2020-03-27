import unittest

from power_dict.errors import NoneParameterError
from power_dict.utils import DictUtils


class GetStrDictPropertyTests(unittest.TestCase):
    properties = {
        "property_1": "Hello!",
        "property_1_none": None,
        "property_1_empty": ''
    }

    def test_get_property(self):
        target = DictUtils.get_str_dict_property(self.properties, 'property_1')
        self.assertIsInstance(target, str)
        self.assertEqual(target, "Hello!")

        target = DictUtils.get_str_dict_property(self.properties, 'property_1_none', default_value="Default string")
        self.assertIsInstance(target, str)
        self.assertEqual(target, "Default string")

        target = DictUtils.get_str_dict_property(self.properties, 'property_1_empty', default_value="Default string")
        self.assertIsInstance(target, str)
        self.assertEqual(target, "Default string")

        target = DictUtils.get_str_dict_property(self.properties, 'key_not_found')
        self.assertIsInstance(target, str)
        self.assertEqual(target, '')

    def test_get_required_property(self):
        target = DictUtils.get_required_str_dict_property(self.properties, 'property_1')
        self.assertIsInstance(target, str)
        self.assertEqual(target, "Hello!")

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_str_dict_property(self.properties, 'property_1_none',
                                                     required_error="Key property_1_none is None")

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_str_dict_property(self.properties, 'property_1_empty',
                                                     required_error="Key property_1_none is None")

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_str_dict_property(self.properties, 'key_not_found')
