from django.db.models import Q
from django.contrib.auth import get_user_model

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import (
        AllowAny,
        IsAdminUser,
    )

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )
from rest_framework.generics import (
        CreateAPIView,
        RetrieveAPIView,
        RetrieveUpdateAPIView,
        UpdateAPIView,
        DestroyAPIView,
        ListAPIView,
    )

from apis.permissions import (
        IsOwnerOrReadOnly,
    )

from apis.serializers import (
        UserCreateSerializer,
        UserLoginSerializer,
        UserModelSerializer,
        UserEditSerializer,
    )

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsAdminUser]


class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsOwnerOrReadOnly]


class UserEditAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserEditSerializer
    # permission_classes = [IsOwnerOrReadOnly]
    lookup_field = "pk"

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        alcohol_tag = request.data.pop('alcohol_tag')
        food_tag = request.data.pop('food_tag')
        place_tag = request.data.pop('place_tag')
        
        atag = AlcoholTag.objects.get(id=alcohol_tag['id'])
        ftag = FoodTag.objects.get(id=food_tag['id'])
        ptag = PlaceTag.objects.get(id=place_tag['id'])

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        instance.alcoholtag_set.add(atag)
        instance.foodtag_set.add(ftag)
        instance.placetag_set.add(ptag)
        from IPython import embed; embed()

        return Response(serializer.data) 
