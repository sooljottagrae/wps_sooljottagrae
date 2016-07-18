from django.conf.urls import url

from apis.views.comment import *

urlpatterns = [
        url(r'^$', CommentListAPIView.as_view(), name="list"),
        url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name="detail"),
        ]
