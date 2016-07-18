from django.conf.urls import url, include

urlpatterns = [
        url(r'users/', include('apis.urls.users', namespace="users")),
        url(r'posts/', include('apis.urls.posts', namespace="posts")),
        url(r'comments/', include('apis.urls.comments', namespace="comments")),
        url(r'tokens/', include('apis.urls.tokens', namespace="tokens")),
]
