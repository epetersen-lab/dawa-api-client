# -*- coding: utf-8 -*-


class ApiError(Exception):
    pass


class ApiErrorConnection(ApiError):
    pass


class ApiErrorNotFound(ApiError):
    pass


class ApiErrorUnknown(ApiError):
    pass


class ApiErrorMessage(ApiError):
    """
    An exception occurred while handling the request.
    It contains details provided by the remote end.
    """

    def __init__(self, title: str, type_: str, details: str):
        self.title: str = title
        self.type_: str = type_
        self.details: str = details

    def __str__(self):
        return f"Title: {self.title}, Type: {self.type_}, Details: {self.details}"


class ApiErrorResourceNotFound(ApiErrorMessage):
    pass


class ApiErrorQueryParameterFormat(ApiErrorMessage):
    pass


class ApiErrorInternalServer(ApiErrorMessage):
    pass
