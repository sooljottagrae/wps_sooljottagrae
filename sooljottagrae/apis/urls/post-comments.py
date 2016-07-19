from django.conf.urls import url

from apis.views.comment import *

urlpatterns = [
        url(r'^$', CommentSpecificListAPIView.as_view(), name="list"),
        url(r'^create/$', CommentCreateAPIView.as_view(), name="create"),
        url(r'^(?P<id>\d+)/$', CommentDetailAPIView.as_view(), name="detail"),
        url(r'^(?P<id>\d+)/edit$', CommentEditAPIView.as_view(), name="edit"),
        ]
