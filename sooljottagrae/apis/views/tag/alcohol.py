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

from tags.models import AlcoholTag

from apis.serializers import AlcoholTagSerializer

from rest_framework.response import Response
from rest_framework import status


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
