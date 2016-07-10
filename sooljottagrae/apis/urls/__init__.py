from django.conf.urls import url, include

from apis.views import *

urlpatterns = [
        url(r'users/', include('apis.urls.users', namespace="users")),
        url(r'posts/', include('apis.urls.posts', namespace="posts")),
        url(r'tokens/', include('apis.urls.tokens', namespace="tokens")),
]
