from django.conf.urls import url, include

from apis.views.comment import CommentGeneralListAPIView

urlpatterns = [
        url(r'users/', include('apis.urls.users', namespace="users")),
        url(r'posts/', include('apis.urls.posts', namespace="posts")),
        url(r'tokens/', include('apis.urls.tokens', namespace="tokens")),
        url(r'comments/', include('apis.urls.comments', namespace="comments")),
        url(r'tags/', include('apis.urls.tags', namespace="tags")),
]
