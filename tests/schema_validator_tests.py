import unittest
from datetime import datetime, date
from decimal import Decimal
from power_dict.schema_validator import SchemaValidator


class SchemaValidatorTests(unittest.TestCase):
    schema = [
        {'name': 'username', 'type': "str", 'required': True, 'description': 'Login',
         'required_error': 'User login is not specified'},
        {'name': 'age', 'type': "int", 'required': False, 'description': 'Age'},
        {'name': 'body_temperature', 'type': "float", 'required': False, "default_value": 36.6},
        {'name': 'balance', 'type': "decimal", 'required': True, 'description': 'Credit card balance'},
        {'name': 'password', 'type': "object", 'required': True, 'description': 'Password',
         'required_error': 'User password is not specified'},
        {'name': 'gender', 'type': "enum", 'required': False, 'choices': ['male', 'female']},
        {'name': 'date_of_birth', 'type': "date", 'required': False},
        {'name': 'last_login', 'type': "datetime", 'required': False},
        {'name': 'is_admin', 'type': "bool", 'required': False, "default_value": False},
        {'name': 'roles', 'type': "list", 'required': True},
    ]

    def test_validate(self):
        context = {
            'username': "login_1",
            'age': "28",
            'body_temperature': "36.6",
            'balance': "1999.99",
            'password': "********",
            'gender': "male",
            'date_of_birth': "2018-11-23",
            'last_login': "2018-11-23 01:45:59",
            'is_admin': "yes",
            'roles': ["user", "super_user"],
        }
        target = SchemaValidator.validate(context, self.schema)

        self.assertIsInstance(target, dict)
        self.assertTrue('username' in target)
        self.assertEqual(target['username'], "login_1")
        self.assertTrue('age' in target)
        self.assertEqual(target['age'], 28)
        self.assertTrue('body_temperature' in target)
        self.assertEqual(target['body_temperature'], 36.6)
        self.assertTrue('balance' in target)
        self.assertEqual(target['balance'], Decimal('1999.99'))
        self.assertTrue('password' in target)
        self.assertEqual(target['password'], '********')
        self.assertTrue('gender' in target)
        self.assertEqual(target['gender'], 'male')
        self.assertTrue('date_of_birth' in target)
        self.assertEqual(target['date_of_birth'], date(2018, 11, 23))
        self.assertTrue('last_login' in target)
        self.assertEqual(target['last_login'], datetime(2018, 11, 23, 1, 45, 59))
        self.assertTrue('is_admin' in target)
        self.assertEqual(target['is_admin'], True)
        self.assertTrue('roles' in target)
        self.assertEqual(target['roles'], ["user", "super_user"])
