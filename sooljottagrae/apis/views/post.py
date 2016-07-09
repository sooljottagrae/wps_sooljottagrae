from rest_framework.generics import ListAPIView, RetrieveAPIView

from posts.models import Post
from apis.serializers import PostModelSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    pk = "post_id"
    serializer_class = PostModelSerializer
