from django.db.models import Q
from django.contrib.auth import get_user_model

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

from apis.serializers import PostListSerializer
from apis.permissions import (
        IsOwnerOrReadOnly,
    )


User = get_user_model()


class MytagsListAPIView(ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self, *args, **kwargs):
        user = User.objects.get(id=self.kwargs.get("pk"))

        alcohol_tag = user.alcoholtag_set.all()
        food_tag = user.foodtag_set.all()
        place_tag = user.placetag_set.all()

        post_queryset = []

        for tag in alcohol_tag:
            posts = tag.post_set.all()
            for post in posts:
                post_queryset.append(post)

        for tag in food_tag:
            posts = tag.post_set.all()
            for post in posts:
                post_queryset.append(post)

        for tag in place_tag:
            posts = tag.post_set.all()
            for post in posts:
                post_queryset.append(post)

        return post_queryset
