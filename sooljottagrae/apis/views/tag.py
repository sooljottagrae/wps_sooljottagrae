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


class AlcoholTagListAPIView(ListAPIView):
    serializer_class = AlcoholTagSerializer
    queryset = AlcoholTag.objects.all()


class FoodTagListAPIView(ListAPIView):
    serializer_class = FoodTagSerializer
    queryset = FoodTag.objects.all()


class PlaceTagListAPIView(ListAPIView):
    serializer_class = PlaceTagSerializer
    queryset = PlaceTag.objects.all()
