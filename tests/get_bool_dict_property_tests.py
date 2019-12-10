import unittest

from power_dict.errors import NoneParameterError, InvalidParameterError
from power_dict.utils import DictUtils


class GetBoolDictPropertyTests(unittest.TestCase):
    properties = {
        "property_1": "1",
        "property_2": 1,
        "property_3": 't',
        "property_4": 'true',
        "property_5": 'yes',
        "property_6": "0",
        "property_7": 0,
        "property_8": 'f',
        "property_9": 'false',
        "property_10": 'no',
        "error": "oops..",
        "property_1_none": None
    }

    def test_get_property(self):
        target = DictUtils.get_bool_dict_property(self.properties, 'property_1')
        self.assertIsInstance(target, bool)
        self.assertEqual(target, True)

        target = DictUtils.get_bool_dict_property(self.properties, 'property_2')
        self.assertIsInstance(target, bool)
        self.assertEqual(target, True)

        target = DictUtils.get_bool_dict_property(self.properties, 'property_3')
        self.assertIsInstance(target, bool)
        self.assertEqual(target, True)

        target = DictUtils.get_bool_dict_property(self.properties, 'property_4')
        self.assertIsInstance(target, bool)
        self.assertEqual(target, True)

        target = DictUtils.get_bool_dict_property(self.properties, 'property_5')
        self.assertIsInstance(target, bool)
        self.assertEqual(target, True)

        target = DictUtils.get_bool_dict_property(self.properties, 'property_6')
        self.assertIsInstance(target, bool)
        self.assertEqual(target, False)

        target = DictUtils.get_bool_dict_property(self.properties, 'property_7')
        self.assertIsInstance(target, bool)
        self.assertEqual(target, False)

        target = DictUtils.get_bool_dict_property(self.properties, 'property_8')
        self.assertIsInstance(target, bool)
        self.assertEqual(target, False)

        target = DictUtils.get_bool_dict_property(self.properties, 'property_9')
        self.assertIsInstance(target, bool)
        self.assertEqual(target, False)

        target = DictUtils.get_bool_dict_property(self.properties, 'property_10')
        self.assertIsInstance(target, bool)
        self.assertEqual(target, False)

        target = DictUtils.get_bool_dict_property(self.properties, 'property_1_none', default_value='yes')
        self.assertIsInstance(target, bool)
        self.assertEqual(target, True)

        target = DictUtils.get_bool_dict_property(self.properties, 'key_not_found')
        self.assertEqual(target, None)

        with self.assertRaises(InvalidParameterError):
            DictUtils.get_bool_dict_property(self.properties, 'error')

    def test_get_required_property(self):
        target = DictUtils.get_required_bool_dict_property(self.properties, 'property_1')
        self.assertIsInstance(target, bool)
        self.assertEqual(target, True)

        target = DictUtils.get_required_bool_dict_property(self.properties, 'property_2')
        self.assertIsInstance(target, bool)
        self.assertEqual(target, True)

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_bool_dict_property(self.properties, 'property_1_none',
                                                     required_error="Key property_1_none is None")

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_bool_dict_property(self.properties, 'key_not_found')

        with self.assertRaises(InvalidParameterError):
            DictUtils.get_required_bool_dict_property(self.properties, 'error')
