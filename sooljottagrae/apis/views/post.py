from django.db.models import Q

from rest_framework.filters import(
        SearchFilter,
        OrderingFilter,
)
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
        ListAPIView,
        CreateAPIView,
        RetrieveAPIView,
        UpdateAPIView,
        RetrieveUpdateAPIView,
        DestroyAPIView,
)

from rest_framework.permissions import (
        AllowAny,
        IsAuthenticated,
        IsAdminUser,
        IsAuthenticatedOrReadOnly,
)

from posts.models import Post

from apis.serializers import (
        PostCreateSerializer,
        PostEditSerializer,
        PostListSerializer,
        PostDetailSerializer,
)

from apis.permissions import IsOwnerOrReadOnly
from apis.views.pagination import (
    PostPageNumberPagination,
)


class PostListAPIView(ListAPIView):
    # queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['content', 'user__email']
    ordering_fields = '__all__'

    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(content__icontains=query) |
                    Q(user__email__icontains=query)
                    ).distinct()
        return queryset_list


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostEditAPIView(RetrieveAPIView, UpdateModelMixin, DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostEditSerializer
    lookup_field = "pk"
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PostDetailAPIView(RetrieveAPIView):
    serializer = PostDetailSerializer()
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = "pk"
