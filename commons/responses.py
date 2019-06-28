class APIResponse:

    @staticmethod
    def result(message=None, data=None):
        return {
            'message': message, 'data': data
        }


class APIPaginatedResponse:

    @staticmethod
    def result(data, count, message=None):
        return {
            'message': message, 'data': data, 'total_count': count
        }
