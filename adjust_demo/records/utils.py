from rest_framework import status
from rest_framework.response import Response

DEFAULT_FAILURE_MESSAGE = 'Unexpected error has occurred'
DEFAULT_SUCCESS_MESSAGE = 'successful'


def success_response(data=None, success_message=DEFAULT_SUCCESS_MESSAGE, status_code=status.HTTP_200_OK):
    response_data = {
        'success': True,
        'message': success_message,
        'data': data
    }
    return Response(response_data, status=status_code)


def failure_response(failure_message=DEFAULT_FAILURE_MESSAGE,status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                     data=None):
    response_data = {
        'status_code': status_code,
        'success': False,
        'message': failure_message,
        'data': data
    }
    return Response(response_data, status=status_code)

