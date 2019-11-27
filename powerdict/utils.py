import datetime
from try_parse.utils import ParseUtils
from decimal import Decimal

from powerdict.errors import InvalidParameterError


class Utils:
    @staticmethod
    def get_setting_by_path(parent_setting, path: str, default_value=None):
        if not Utils.str_is_null_or_empty(path) and parent_setting is not None:
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
        if properties is None or Utils.str_is_null_or_empty(key):
            return default_value

        if key in properties:
            v = properties[key]
            if v is None:
                return default_value
            else:
                return v

        return default_value

    @staticmethod
    def get_required_dict_property(properties: dict, key: str, required_error=None):
        value = Utils.get_dict_property(properties, key)

        if value is not None:
            return value

        Utils.raise_none_parameter_error(key, required_error)

    @staticmethod
    def get_str_dict_property(properties: dict, key: str, default_value='') -> str:
        value = Utils.get_dict_property(properties, key)

        if Utils.str_is_null_or_empty(value):
            if default_value is None:
                return None
            value = default_value

        return str(value).strip()

    @staticmethod
    def get_required_str_dict_property(properties: dict, key: str, required_error=None) -> str:
        value = Utils.get_str_dict_property(properties, key)

        if Utils.str_is_null_or_empty(value):
            Utils.raise_none_parameter_error(key, required_error)

        return value

    @staticmethod
    def get_int_dict_property(properties: dict, key: str, default_value=None) -> int:
        value = Utils.get_dict_property(properties, key)

        if Utils.str_is_null_or_empty(value):
            value = default_value

        status, result = utils.Utils ParseUtils.try_parse_int(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в число')

    @staticmethod
    def get_required_int_dict_property(properties: dict, key: str, required_error=None) -> int:
        value = Utils.get_dict_property(properties, key)

        if Utils.str_is_null_or_empty(value):
            Utils.raise_none_parameter_error(key, required_error)

        status, result = ParseUtils.try_parse_int(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в число')

    @staticmethod
    def get_datetime_dict_property(properties: dict, key: str, default_value: datetime = None) -> datetime:
        value = Utils.get_dict_property(properties, key)

        if Utils.str_is_null_or_empty(value):
            value = default_value

        status, result = ParseUtils.try_parse_datetime(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в дату и время')

    @staticmethod
    def get_required_datetime_dict_property(properties: dict, key: str, required_error=None) -> datetime:
        value = Utils.get_dict_property(properties, key)

        if Utils.str_is_null_or_empty(value):
            Utils.raise_none_parameter_error(key, required_error)

        status, result = ParseUtils.try_parse_datetime(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в дату и время')

    @staticmethod
    def get_date_dict_property(properties: dict, key: str, default_value=None) -> datetime.date:
        value = Utils.get_dict_property(properties, key)

        if Utils.str_is_null_or_empty(value):
            value = default_value

        status, result = ParseUtils.try_parse_date(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в дату')

    @staticmethod
    def get_required_date_dict_property(properties: dict, key: str, required_error=None) -> datetime.date:
        value = Utils.get_dict_property(properties, key)

        if Utils.str_is_null_or_empty(value):
            Utils.raise_none_parameter_error(key, required_error)

        status, result = Utils.try_parse_date(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в дату')

    @staticmethod
    def get_bool_dict_property(properties: dict, key: str, default_value=None) -> bool:
        value = Utils.get_dict_property(properties, key)

        if Utils.str_is_null_or_empty(value):
            value = default_value

        status, result = ParseUtils.try_parse_bool(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в тип bool')

    @staticmethod
    def get_required_bool_dict_property(properties: dict, key: str, required_error=None) -> bool:
        value = Utils.get_dict_property(properties, key)

        if Utils.str_is_null_or_empty(value):
            Utils.raise_none_parameter_error(key, required_error)

        status, result = ParseUtils.try_parse_bool(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в тип bool')

    @staticmethod
    def get_decimal_dict_property(properties: dict, key: str, default_value=None) -> Decimal:
        value = Utils.get_dict_property(properties, key)

        if Utils.str_is_null_or_empty(value):
            value = default_value

        status, result = ParseUtils.try_parse_decimal(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в число')

    @staticmethod
    def get_required_decimal_dict_property(properties: dict, key: str, required_error=None) -> Decimal:
        value = Utils.get_dict_property(properties, key)

        if Utils.str_is_null_or_empty(value):
            Utils.raise_none_parameter_error(key, required_error)

        status, result = ParseUtils.try_parse_decimal(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в число')

    @staticmethod
    def get_list_dict_property(properties: dict, key: str, default_value=None) -> list:
        v = Utils.get_dict_property(properties, key)
        if v is None:
            return default_value
        else:
            return list(v)

    @staticmethod
    def get_required_list_dict_property(properties: dict, key: str) -> list:
        v = Utils.get_required_dict_property(properties, key)

        return list(v)

    @staticmethod
    def raise_none_parameter_error(key=None, error=None):
        if error is not None:
            message = error
        elif key is not None:
            message = f'Параметр "{key}" не указан'
        else:
            message = f'Параметр не указан'

        raise NoneParameterError(message)

    @staticmethod
    def get_float_dict_property(properties: dict, key: str, default_value=None) -> float:
        value = Utils.get_dict_property(properties, key)

        if Utils.str_is_null_or_empty(value):
            value = default_value

        status, result = ParseUtils.try_parse_float(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в число')

    @staticmethod
    def get_required_float_dict_property(properties: dict, key: str, required_error=None) -> float:
        value = Utils.get_dict_property(properties, key)

        if Utils.str_is_null_or_empty(value):
            Utils.raise_none_parameter_error(key, required_error)

        status, result = ParseUtils.try_parse_float(value)
        if status:
            return result
        else:
            raise InvalidParameterError('Параметр "' + key + '" не удалось преобразовать в число')

    @staticmethod
    def str_is_null_or_empty(text) -> bool:
        return text is None or not str(text).strip()
