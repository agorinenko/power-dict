import unittest

from power_dict.utils import DictUtils


class GetSettingByPathTests(unittest.TestCase):
    properties = {
        "object2": {
            "object_2.1": 1,
            "object_2.2": {
                "object_2.2.1": 2.1
            }
        },
        "str_2": {
            "str_3": "qwerty"
        },
        "list": [1, 2, 3],
    }

    def test_get_setting_by_path(self):
        target = DictUtils.get_setting_by_path(self.properties, 'object2->object_2.2->object_2.2.1', separator="->",
                                               data_type="float")
        self.assertIsInstance(target, float)
        self.assertEqual(target, 2.1)

        target = DictUtils.get_setting_by_path(self.properties, 'object2->object_2.2->key_not_found', separator="->",
                                               data_type="float", default_value=2.2)
        self.assertIsInstance(target, float)
        self.assertEqual(target, 2.2)

        target = DictUtils.get_setting_by_path(self.properties, 'list', data_type="list")
        self.assertIsInstance(target, list)
        self.assertEqual(target, [1, 2, 3])

        target = DictUtils.get_setting_by_path(self.properties, 'str_2.str_3')
        self.assertIsInstance(target, str)
        self.assertEqual(target, "qwerty")
