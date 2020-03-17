from try_parse.utils import ParseUtils

from power_dict.errors import InvalidSchemeError
from power_dict.utils import DictUtils


def empty_list(item_schema: dict, value):
    if isinstance(value, list):
        required = DictUtils.get_bool_dict_property(item_schema, 'required', default_value=False)
        empty = DictUtils.get_bool_dict_property(item_schema, 'empty', default_value=True)

        if not required and not empty:
            raise InvalidSchemeError(
                "A schema conflict. The combination of properties required=False and empty=False is not allowed.")

        if required and not empty and len(value) == 0:
            raise InvalidSchemeError(
                "The list can't be empty.")

    return value


def unique_list(item_schema: dict, value):
    if isinstance(value, list):
        unique = DictUtils.get_bool_dict_property(item_schema, 'unique', default_value=False)

        if unique is not None:
            value = list(set(value))

    return value

def items_list(item_schema: dict, value):
    if isinstance(value, list):
        items = DictUtils.get_dict_property(item_schema, 'items')

        def __convert(item):
            item_type = DictUtils.get_str_dict_property(items, 'type', 'str')
            def __convert_enum(str_value):
                choices = DictUtils.get_required_list_dict_property(items, 'choices', 'str')
                if str_value is not None and str_value not in choices:
                    raise InvalidSchemeError(
                        f"The value '{str_value}' is not available for selection. Possible options: {choices}")

                return True, str_value

            map_func = {
                "enum": __convert_enum,
                "str": lambda x: (True, str(x)),
                "int": ParseUtils.try_parse_int,
                "datetime": ParseUtils.try_parse_datetime,
                "date": ParseUtils.try_parse_date,
                "bool": ParseUtils.try_parse_bool,
                "decimal": ParseUtils.try_parse_decimal,
                "float": ParseUtils.try_parse_float
            }

            if item_type not in map_func:
                return item

            func = map_func[item_type]
            success, __value = func(item)
            return __value if success else None


        if items is not None:
            new_value = list(list(map(__convert, value)))
            return new_value

    return value
