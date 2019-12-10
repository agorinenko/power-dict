import unittest

from power_dict.errors import NoneParameterError
from power_dict.utils import DictUtils


class GetListDictPropertyTests(unittest.TestCase):
    properties = {
        "property_1": [1, 2, 3],
        "property_1_none": None
    }

    def test_get_property(self):
        target = DictUtils.get_list_dict_property(self.properties, 'property_1')
        self.assertIsInstance(target, list)
        self.assertEqual(target, [1, 2, 3])

        target = DictUtils.get_list_dict_property(self.properties, 'property_1_none', default_value=[4, 5, 6])
        self.assertIsInstance(target, list)
        self.assertEqual(target, [4, 5, 6])

        target = DictUtils.get_list_dict_property(self.properties, 'key_not_found')
        self.assertEqual(target, None)

    def test_get_required_property(self):
        target = DictUtils.get_required_list_dict_property(self.properties, 'property_1')
        self.assertIsInstance(target, list)
        self.assertEqual(target, [1, 2, 3])

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_list_dict_property(self.properties, 'property_1_none',
                                                      required_error="Key property_1_none is None")

        with self.assertRaises(NoneParameterError):
            DictUtils.get_required_list_dict_property(self.properties, 'key_not_found')
