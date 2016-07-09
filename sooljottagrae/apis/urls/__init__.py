from django.conf.urls import url, include

from apis.views import *

urlpatterns = [
        url(r'^posts/$', PostListAPIView.as_view(), name="post-list"),
        url(r'^posts/create/$', PostCreateAPIView.as_view(), name="post-create"),
        url(r'^posts/(?P<pk>\w+)/$', PostDetailAPIView.as_view(), name="post-detail"),
        url(r'^posts/(?P<pk>\w+)/edit/$', PostUpdateAPIView.as_view(), name="post-edit"),
        url(r'^posts/(?P<pk>\w+)/delete/$', PostDeleteAPIView.as_view(), name="post-delete"),

        url(r'^users/$', UserListAPIView.as_view(), name="user-list"),
        url(r'^users/(?P<pk>\w+)/$', UserDetailAPIView.as_view(), name="user-detail"),

        url(r'token/', include('apis.urls.tokens', namespace="tokens")),
        ]
