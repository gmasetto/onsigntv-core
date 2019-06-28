from rest_framework import status
from rest_framework.exceptions import APIException


class OnSignTvException(APIException):
    def __init__(self, error=None, data=None, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR):
        super().__init__(data)
        self.error = error
        self.data = data
        self.detail = {'message': error, 'data': data}
        self.status_code = status_code

    def __str__(self):
        import json
        return json.dumps(self.detail)
