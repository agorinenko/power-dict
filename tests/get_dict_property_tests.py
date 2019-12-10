import unittest

from power_dict.errors import NoneParameterError
from power_dict.utils import DictUtils


class GetDictPropertyTests(unittest.TestCase):
    properties = {
        "property_1": {
            "object_1": 1
        },
        "property_1_none": None
    }

    def test_get_property(self):
        target = DictUtils.get_dict_property(self.properties, 'property_1')
        self.assertIsInstance(target, object)
        self.assertEqual(target, {"object_1": 1})

        target = DictUtils.get_dict_property(self.properties, 'property_1_none', default_value={"object_2": 2})
        self.assertIsInstance(target, object)
        self.assertEqual(target, {"object_2": 2})

        target = DictUtils.get_dict_property(self.properties, 'key_not_found')
        self.assertIsInstance(target, object)
        self.assertEqual(target, None)

    def test_get_required_property(self):
        target = DictUtils.get_required_dict_property(self.properties, 'property_1')
        self.assertIsInstance(target, object)
        self.assertEqual(target, {"object_1": 1})

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_dict_property(self.properties, 'property_1_none',
                                                 required_error="Key property_1_none is None")

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_dict_property(self.properties, 'key_not_found')
