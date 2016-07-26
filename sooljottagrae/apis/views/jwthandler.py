from rest_framework_jwt.utils import jwt_response_payload_handler

from apis.serializers.user import UserModelSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserModelSerializer(user, context={'request': request}).data
    }
