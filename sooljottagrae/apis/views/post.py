from rest_framework.generics import (
        ListAPIView,
        RetrieveAPIView,
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
    pk = "post_id"
    serializer_class = PostDetailSerializer
