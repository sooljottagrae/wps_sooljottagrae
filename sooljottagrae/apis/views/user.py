from rest_framework.generics import ListAPIView, RetrieveAPIView

from users.models import User
from apis.serializers import UserModelSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    pk = "id"
    serializer_class = UserModelSerializer
