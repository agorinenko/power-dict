from power_dict.errors import InvalidSchemeError, NotAllowedParameterError
from power_dict.utils import DictUtils


class SchemaValidator:
    @staticmethod
    def validate(context: dict, schema: list, sanitize_schema: bool = True) -> dict:
        """
        Validation and transformation of 'context' dictionary in accordance with the rules of the scheme
        :param context:
        :param schema:
        :param sanitize_schema:
        :return:
        """
        if sanitize_schema:
            schema_keys = SchemaValidator.__get_schema_keys(schema)
            SchemaValidator.__sanitize_schema(context, schema_keys)

        return SchemaValidator.__transform_context(context, schema)

    @staticmethod
    def __get_schema_keys(schema: list) -> set:
        keys = set()

        if schema is None or len(schema) == 0:
            return keys

        for item in schema:
            name = DictUtils.get_required_dict_property(item, 'name')
            if name in keys:
                raise InvalidSchemeError(f"The parameter '{name}' is repeated")

            keys.add(name)

        return keys

    @staticmethod
    def __sanitize_schema(context: dict, keys: set):
        context_keys = context.keys()
        for key in context_keys:
            if key not in keys:
                raise NotAllowedParameterError(f"The parameter '{key}' is not allowed")

    @staticmethod
    def __transform_context(context: dict, schema: list) -> dict:
        if schema is None or len(schema) == 0:
            return context

        new_context = {}
        for item in schema:
            name = DictUtils.get_required_dict_property(item, 'name')

            value = SchemaValidator.__get_item_value(item, context)

            if SchemaValidator.__check_user_validators(item, value):
                new_context[name] = value

        return new_context

    @staticmethod
    def __get_item_value(item, context: dict):
        item_type = DictUtils.get_str_dict_property(item, 'type', 'str')
        name = DictUtils.get_required_str_dict_property(item, 'name')
        required = DictUtils.get_bool_dict_property(item, 'required', default_value=False)
        default_value = DictUtils.get_dict_property(item, 'default_value')
        required_error = DictUtils.get_str_dict_property(item, 'required_error', None)
        item_format = DictUtils.get_str_dict_property(item, 'format', None)

        if item_type == "enum":
            choices = DictUtils.get_required_list_dict_property(item, 'choices', required_error=required_error)

            if required:
                str_value = DictUtils.get_required_str_dict_property(context, name, required_error=required_error)
            else:
                str_value = DictUtils.get_str_dict_property(context, name, default_value)

            if str_value is not None and str_value not in choices:
                raise InvalidSchemeError(
                    f"The value '{str_value}' is not available for selection. Possible options: {choices}")

            return str_value
        else:
            if required:
                return DictUtils.get_required_value(context, name, data_type=item_type,
                                                    required_error=required_error, format=item_format)
            else:
                return DictUtils.get_value(context, name, data_type=item_type,
                                           default_value=default_value, format=item_format)

    @staticmethod
    def __check_user_validators(item_schema: dict, value):
        if value is None or item_schema is None:
            return True

        validators = DictUtils.get_list_dict_property(item_schema, 'validators')

        if validators is not None and len(validators) > 0:
            name = DictUtils.get_required_dict_property(item_schema, 'name')

            for validator in validators:
                error = None
                if not callable(validator):
                    message = DictUtils.get_str_dict_property(validator, 'message')
                    validator = DictUtils.get_required_dict_property(validator, 'f')

                    if not DictUtils.str_is_null_or_empty(value) and '#VALUE#' in message:
                        message = message.replace('#VALUE#', str(value))

                    error = f"{message}"

                if callable(validator) and not validator(value):
                    if error is None:
                        error = f"The parameter '{name} does not match the specified condition"

                    raise InvalidSchemeError(error)

        return True
