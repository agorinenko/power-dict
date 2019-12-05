import datetime
from try_parse.utils import ParseUtils
from decimal import Decimal

from power_dict.errors import InvalidParameterError, NoneParameterError


class DictUtils:
    __MAP = {
        object: lambda x: DictUtils.get_dict_property,
        str: lambda x: DictUtils.get_str_dict_property,
        int: lambda x: DictUtils.get_int_dict_property,
        datetime: lambda x: DictUtils.get_datetime_dict_property,
        datetime.date: lambda x: DictUtils.get_date_dict_property,
        bool: lambda x: DictUtils.get_bool_dict_property,
        Decimal: lambda x: DictUtils.get_decimal_dict_property,
        list: lambda x: DictUtils.get_list_dict_property,
        float: lambda x: DictUtils.get_float_dict_property
    }

    @staticmethod
    def get_setting_by_path(parent_setting, path: str, default_value=None, data_type=None):
        if not DictUtils.str_is_null_or_empty(path) and parent_setting is not None:
            ps = path.split('.')
            i = 0
            ps_len = len(ps)

            if ps_len > 0:
                for p in ps:
                    i = i + 1

                    if parent_setting is not None and p in parent_setting:
                        parent_setting = parent_setting[p]
                        if i == ps_len:
                            if parent_setting is None:
                                return default_value

                            return parent_setting

        return None

    @staticmethod
    def get_dict_property(properties: dict, key: str, default_value=None) -> object:
        if properties is None or DictUtils.str_is_null_or_empty(key):
            return default_value

        if key in properties:
            v = properties[key]
            if v is None:
                return default_value
            else:
                return v

        return default_value

    @staticmethod
    def get_required_dict_property(properties: dict, key: str, required_error=None) -> object:
        value = DictUtils.get_dict_property(properties, key)

        if value is not None:
            return value

        DictUtils.raise_none_parameter_error(key, required_error)

    @staticmethod
    def get_str_dict_property(properties: dict, key: str, default_value='') -> str:
        value = DictUtils.get_dict_property(properties, key)

        if DictUtils.str_is_null_or_empty(value):
            if default_value is None:
                return None
            value = default_value

        return str(value).strip()

    @staticmethod
    def get_required_str_dict_property(properties: dict, key: str, required_error=None) -> str:
        value = DictUtils.get_required_dict_property(properties, key, required_error)

        return str(value)

    @staticmethod
    def get_int_dict_property(properties: dict, key: str, default_value=None) -> int:
        value = DictUtils.get_dict_property(properties, key)

        if DictUtils.str_is_null_or_empty(value):
            value = default_value

        status, result = ParseUtils.try_parse_int(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в число')

    @staticmethod
    def get_required_int_dict_property(properties: dict, key: str, required_error=None) -> int:
        value = DictUtils.get_required_dict_property(properties, key, required_error)

        status, result = ParseUtils.try_parse_int(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в число')

    @staticmethod
    def get_datetime_dict_property(properties: dict, key: str, default_value: datetime = None) -> datetime:
        value = DictUtils.get_dict_property(properties, key)

        if DictUtils.str_is_null_or_empty(value):
            value = default_value

        status, result = ParseUtils.try_parse_datetime(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в дату и время')

    @staticmethod
    def get_required_datetime_dict_property(properties: dict, key: str, required_error=None) -> datetime:
        value = DictUtils.get_required_dict_property(properties, key, required_error)

        status, result = ParseUtils.try_parse_datetime(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в дату и время')

    @staticmethod
    def get_date_dict_property(properties: dict, key: str, default_value=None) -> datetime.date:
        value = DictUtils.get_dict_property(properties, key)

        if DictUtils.str_is_null_or_empty(value):
            value = default_value

        status, result = ParseUtils.try_parse_date(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в дату')

    @staticmethod
    def get_required_date_dict_property(properties: dict, key: str, required_error=None) -> datetime.date:
        value = DictUtils.get_required_dict_property(properties, key, required_error)

        status, result = ParseUtils.try_parse_date(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в дату')

    @staticmethod
    def get_bool_dict_property(properties: dict, key: str, default_value=None) -> bool:
        value = DictUtils.get_dict_property(properties, key)

        if DictUtils.str_is_null_or_empty(value):
            value = default_value

        status, result = ParseUtils.try_parse_bool(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в тип bool')

    @staticmethod
    def get_required_bool_dict_property(properties: dict, key: str, required_error=None) -> bool:
        value = DictUtils.get_required_dict_property(properties, key, required_error)
        status, result = ParseUtils.try_parse_bool(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в тип bool')

    @staticmethod
    def get_decimal_dict_property(properties: dict, key: str, default_value=None) -> Decimal:
        value = DictUtils.get_dict_property(properties, key)

        if DictUtils.str_is_null_or_empty(value):
            value = default_value

        status, result = ParseUtils.try_parse_decimal(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в число')

    @staticmethod
    def get_required_decimal_dict_property(properties: dict, key: str, required_error=None) -> Decimal:
        value = DictUtils.get_required_dict_property(properties, key, required_error)

        status, result = ParseUtils.try_parse_decimal(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в число')

    @staticmethod
    def get_list_dict_property(properties: dict, key: str, default_value=None) -> list:
        v = DictUtils.get_dict_property(properties, key)
        if v is None:
            return default_value
        else:
            return list(v)

    @staticmethod
    def get_required_list_dict_property(properties: dict, key: str, required_error=None) -> list:
        required_object = DictUtils.get_required_dict_property(properties, key, required_error)

        return list(required_object)

    @staticmethod
    def get_float_dict_property(properties: dict, key: str, default_value=None) -> float:
        value = DictUtils.get_dict_property(properties, key)

        if DictUtils.str_is_null_or_empty(value):
            value = default_value

        status, result = ParseUtils.try_parse_float(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в число')

    @staticmethod
    def get_required_float_dict_property(properties: dict, key: str, required_error=None) -> float:
        value = DictUtils.get_required_dict_property(properties, key, required_error)

        status, result = ParseUtils.try_parse_float(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в число')

    @staticmethod
    def str_is_null_or_empty(text) -> bool:
        return text is None or not str(text).strip()

    @staticmethod
    def raise_none_parameter_error(key=None, error=None):
        if error is not None:
            message = error
        elif key is not None:
            message = f'Параметр "{key}" не указан'
        else:
            message = f'Параметр не указан'

        raise NoneParameterError(message)
