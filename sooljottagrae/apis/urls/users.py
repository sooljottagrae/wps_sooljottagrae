from django.conf.urls import url

from apis.views import *

urlpatterns = [
        url(r'^$', UserListAPIView.as_view(), name="list"),
        url(r'^(?P<pk>\w+)/$', UserDetailAPIView.as_view(), name="detail"),
]
