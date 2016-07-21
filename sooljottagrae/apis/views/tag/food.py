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

from tags.models import FoodTag

from apis.serializers import FoodTagSerializer

from rest_framework.response import Response
from rest_framework import status


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
