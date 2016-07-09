from rest_framework.generics import (
        ListAPIView,
        RetrieveAPIView,
        UpdateAPIView,
        DestroyAPIView,
)

from posts.models import Post

from apis.serializers import (
        PostListSerializer,
        PostDetailSerializer,
)


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    pk = "post_id"


class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
