class InvalidParameterError(Exception):
    """
    Invalid parameter
    """


class NoneParameterError(Exception):
    """
    Parameter is null or empty
    """


class InvalidSchemeError(Exception):
    """
    The scheme was not validated
    """


class NotAllowedParameterError(Exception):
    """
    The parameter is not allowed
    """
