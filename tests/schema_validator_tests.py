import unittest
from datetime import datetime, date
from decimal import Decimal

from power_dict.errors import InvalidSchemeError
from power_dict.schema_validator import SchemaValidator


def date_of_birth_validator(value) -> bool:
    return True


def roles_validator(value) -> bool:
    return True


class SchemaValidatorTests(unittest.TestCase):
    schema = [
        {'name': 'username', 'type': "str", 'required': True, 'description': 'Login',
         'required_error': 'User login is not specified'},
        {'name': 'age', 'type': "int", 'required': False, 'description': 'Age',
         'validators': [lambda v: 0 < v <= 50]},
        {'name': 'body_temperature', 'type': "float", 'required': False, "default_value": 36.6},
        {'name': 'balance', 'type': "decimal", 'required': True, 'description': 'Credit card balance'},
        {'name': 'password', 'type': "object", 'required': True, 'description': 'Password',
         'required_error': 'User password is not specified'},
        {'name': 'gender', 'type': "enum", 'required': False, 'choices': ['male', 'female']},
        {'name': 'date_of_birth', 'type': "date", 'required': False,
         'validators': [{'f': date_of_birth_validator, 'message': 'date_of_birth invalid'}]},
        {'name': 'last_login', 'type': "datetime", 'required': False},
        {'name': 'is_admin', 'type': "bool", 'required': False, "default_value": False},
        {'name': 'roles', 'type': "list", 'required': True, 'validators': [{'f': roles_validator}]},
    ]

    def test_lambda_validator(self):
        context = {
            'username': "login_1",
            'age': "-1",
            'body_temperature': "36.6",
            'balance': "1999.99",
            'password': "********",
            'gender': "male",
            'date_of_birth': "2018-11-23",
            'last_login': "2018-11-23 01:45:59",
            'is_admin': "yes",
            'roles': ["user", "super_user"],
        }
        with self.assertRaises(InvalidSchemeError):
            SchemaValidator.validate(context, self.schema)

    def test_simple_validate_transform(self):
        """
        Simple validate and transform
        :return:
        """
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
        self.assertEqual(target['roles'].sort(), context["roles"].sort())

    def test_list_1(self):
        """
        List validate and transform
        :return:
        """
        list_schema = [
            {'name': 'empty_list', 'type': "list", 'required': True},
        ]
        context = {
            'empty_list': [],
        }
        target = SchemaValidator.validate(context, list_schema)
        self.assertIsInstance(target, dict)
        self.assertEqual(target['empty_list'], [])

    def test_list_2(self):
        """
        List validate and transform
        :return:
        """
        list_schema = [
            {'name': 'empty_list', 'type': "list", 'required': True, 'empty': False},
        ]
        context = {
            'empty_list': [],
        }
        with self.assertRaises(InvalidSchemeError):
            SchemaValidator.validate(context, list_schema)

    def test_list_3(self):
        """
        List validate and transform
        :return:
        """
        list_schema = [
            {'name': 'empty_list', 'type': "list", 'required': False, 'empty': False},
        ]
        context = {
            'empty_list': [],
        }

        with self.assertRaises(InvalidSchemeError):
            SchemaValidator.validate(context, list_schema)

    def test_list_4(self):
        """
        List validate and transform
        :return:
        """
        list_schema = [
            {'name': 'empty_list', 'type': "list", 'required': True, 'empty': False},
        ]
        context = {
            'empty_list': [1, 2, 3],
        }
        target = SchemaValidator.validate(context, list_schema)
        self.assertIsInstance(target, dict)
        self.assertEqual(target['empty_list'], context['empty_list'])

    def test_list_5(self):
        """
        List validate and transform
        :return:
        """
        list_schema = [
            {'name': 'empty_list', 'type': "list", 'unique': True},
        ]
        context = {
            'empty_list': [1, 1, 2, 2, 3, 3],
        }
        target = SchemaValidator.validate(context, list_schema)
        self.assertIsInstance(target, dict)
        self.assertEqual(target['empty_list'], [1, 2, 3])

    def test_list_6(self):
        """
        List validate and transform
        :return:
        """
        list_schema = [
            {
                'name': 'empty_list', 'type': "list", 'unique': True,
                'items': {'type': "enum", 'choices': ['male', 'female']},
            },
        ]
        context = {
            'empty_list': ['male', 'male', 'female', 'female'],
        }
        target = SchemaValidator.validate(context, list_schema)
        self.assertIsInstance(target, dict)
        self.assertEqual(target['empty_list'].sort() , ['male', 'female'].sort())

    def test_list_7(self):
        """
        List validate and transform
        :return:
        """
        list_schema = [
            {
                'name': 'empty_list', 'type': "list", 'unique': True,
                'items': {'type': "int"},
            },
        ]
        context = {
            'empty_list': ['1', '2', '2', '3'],
        }
        target = SchemaValidator.validate(context, list_schema)
        self.assertIsInstance(target, dict)
        self.assertEqual(target['empty_list'], [1, 2, 3])

    def test_list_8(self):
        """
        List validate and transform
        :return:
        """
        list_schema = [
            {
                'name': 'empty_list', 'type': "list", 'unique': True,
                'items': {'type': "enum", 'choices': ['male', 'female']},
            },
        ]
        context = {
            'empty_list': ['male', 'male', 'female', 'female', 'RRRR!'],
        }
        with self.assertRaises(InvalidSchemeError):
            SchemaValidator.validate(context, list_schema)
