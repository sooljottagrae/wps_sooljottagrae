from django.db.models import Q

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
)
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.views import APIView
from rest_framework.generics import (
        ListAPIView,
        CreateAPIView,
        DestroyAPIView,
        ListAPIView,
        UpdateAPIView,
        RetrieveAPIView,
        RetrieveUpdateAPIView,
)

from rest_framework.permissions import (
        AllowAny,
        IsAuthenticated,
        IsAdminUser,
        IsAuthenticatedOrReadOnly,
)

from apis.permissions import IsOwnerOrReadOnly
from apis.views.pagination import PostPageNumberPagination

from tags.models import AlcoholTag, FoodTag, PlaceTag

from apis.serializers import (
        AlcoholTagSerializer,
        FoodTagSerializer,
        PlaceTagSerializer,
)

from rest_framework.response import Response
from rest_framework import status


"""
Alcohol Tag CRUD
"""


class AlcoholTagListAPIView(ListAPIView):
    serializer_class = AlcoholTagSerializer
    queryset = AlcoholTag.objects.all()


class AlcoholTagCreateAPIView(CreateAPIView):
    serializer_class = AlcoholTagSerializer
    queryset = AlcoholTag.objects.all()
    permission_classes = [IsAdminUser]


class AlcoholTagDetailAPIView(RetrieveAPIView):
    serializer_class = AlcoholTagSerializer
    queryset = AlcoholTag.objects.all()


class AlcoholTagUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = AlcoholTagSerializer
    queryset = AlcoholTag.objects.all()
    permission_classes = [IsAdminUser]


class AlcoholTagDeleteAPIView(DestroyAPIView):
    serializer_class = AlcoholTagSerializer
    queryset = AlcoholTag.objects.all()
    permission_classes = [IsAdminUser]


"""
Food Tag CRUD
"""


class FoodTagListAPIView(ListAPIView):
    serializer_class = FoodTagSerializer
    queryset = FoodTag.objects.all()


class FoodTagCreateAPIView(CreateAPIView):
    serializer_class = FoodTagSerializer
    queryset = FoodTag.objects.all()
    permission_classes = [IsAdminUser]


class FoodTagDetailAPIView(RetrieveAPIView):
    serializer_class = FoodTagSerializer
    queryset = FoodTag.objects.all()


class FoodTagUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = FoodTagSerializer
    queryset = FoodTag.objects.all()
    permission_classes = [IsAdminUser]


class FoodTagDeleteAPIView(DestroyAPIView):
    serializer_class = FoodTagSerializer
    queryset = FoodTag.objects.all()
    permission_classes = [IsAdminUser]


"""
PlaceTag CRUD
"""


class PlaceTagListAPIView(ListAPIView):
    serializer_class = PlaceTagSerializer
    queryset = PlaceTag.objects.all()


class PlaceTagCreateAPIView(CreateAPIView):
    serializer_class = PlaceTagSerializer
    queryset = PlaceTag.objects.all()
    permission_classes = [IsAdminUser]


class PlaceTagDetailAPIView(RetrieveAPIView):
    serializer_class = PlaceTagSerializer
    queryset = PlaceTag.objects.all()


class PlaceTagUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = PlaceTagSerializer
    queryset = PlaceTag.objects.all()
    permission_classes = [IsAdminUser]


class PlaceTagDeleteAPIView(DestroyAPIView):
    serializer_class = PlaceTagSerializer
    queryset = PlaceTag.objects.all()
    permission_classes = [IsAdminUser]
