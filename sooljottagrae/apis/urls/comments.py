from django.conf.urls import url

from apis.views.comment import *

urlpatterns = [
        url(r'^$', CommentListAPIView.as_view(), name="list"),

        url(r'^create/$', CommentCreateAPIView.as_view(), name="comment-create"),
        url(r'^(?P<id>\d+)/$', CommentDetailAPIView.as_view(), name="comment-detail"),
        url(r'^(?P<id>\d+)/edit$', CommentEditAPIView.as_view(), name="comment-edit"),
        ]
