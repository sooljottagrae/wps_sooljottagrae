from django.conf.urls import url, include

from apis.views.post import *
# from apis.views.comment import *

urlpatterns = [
        url(r'^$', PostListAPIView.as_view(), name="list"),
        url(r'^create/$', PostCreateAPIView.as_view(), name="create"),
        url(r'^(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name="detail"),
        url(r'^(?P<pk>\d+)/edit/$', PostUpdateAPIView.as_view(), name="edit"),
        url(r'^(?P<pk>\d+)/delete/$', PostDeleteAPIView.as_view(), name="delete"),

        url(r'^(?P<pk>\d+)/comments/', include('apis.urls.post-comments', namespace="comments")),
        ]
