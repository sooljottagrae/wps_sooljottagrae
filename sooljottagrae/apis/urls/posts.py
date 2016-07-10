from django.conf.urls import url

from apis.views import *

urlpatterns = [
        url(r'^posts/$', PostListAPIView.as_view(), name="post-list"),
        url(r'^posts/create/$', PostCreateAPIView.as_view(), name="post-create"),
        url(r'^posts/(?P<pk>\w+)/$', PostDetailAPIView.as_view(), name="post-detail"),
        url(r'^posts/(?P<pk>\w+)/edit/$', PostUpdateAPIView.as_view(), name="post-edit"),
        url(r'^posts/(?P<pk>\w+)/delete/$', PostDeleteAPIView.as_view(), name="post-delete"),
        ]
