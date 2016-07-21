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

from tags.models import PlaceTag

from apis.serializers import PlaceTagSerializer

from rest_framework.response import Response
from rest_framework import status


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
