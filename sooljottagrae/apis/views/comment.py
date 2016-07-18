from django.db.models import Q

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
)

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

from posts.models import Comment
from posts.models import Post

from apis.serializers import (
        CommentSerializer,
        CommentCreateSerializer,
)

from rest_framework.response import Response
from rest_framework import status


class CommentCreateAPIView(APIView):
    serializer_class = CommentCreateSerializer

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(id=self.kwargs.get("pk"))
        comment = post.comment_set.create(
            content=request.POST.get("content"),
            user=request.user,
        )

        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "nickname": request.user.nickname,
                "content": comment.content,
            },
        )


class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['content', 'user__email']
    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Comment.objects.all()
        query = self.request.GET.get("q")

        if query:
            queryset_list = queryset_list.filter(
                    Q(content__icontains=query) |
                    Q(user__email__icontains=query)
                    ).distinct()
        return queryset_list
