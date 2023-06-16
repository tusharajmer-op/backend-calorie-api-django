from rest_framework import status
from rest_framework.exceptions import APIException


class BaseCustomException(APIException):
    detail = None
    status_code = None

    def __init__(self, detail, code):
        super().__init__(detail, code)
        self.detail = detail
        self.status_code = code

class InvalidCustomerRequestException(BaseCustomException):

    def __init__(self, detail):
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)
class MissingUsernameAndPassword(BaseCustomException):
    def __init__(self, detail):
        super().__init__(detail, status.HTTP_206_PARTIAL_CONTENT)
class InvalidRequestType(BaseCustomException):
    def __init__(self, detail):
        super().__init__(detail, status.HTTP_405_METHOD_NOT_ALLOWED)
class generalError(BaseCustomException):
    def __init__(self, detail):
        super().__init__(detail, status.HTTP_405_METHOD_NOT_ALLOWED)
class TokenError(BaseCustomException):
    def __init__(self, detail):
        super().__init__(detail, status.HTTP_405_METHOD_NOT_ALLOWED)