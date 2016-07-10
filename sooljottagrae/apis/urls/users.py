from django.conf.urls import url

from apis.views import *

urlpatterns = [
        url(r'^users/$', UserListAPIView.as_view(), name="user-list"),
        url(r'^users/(?P<pk>\w+)/$', UserDetailAPIView.as_view(), name="user-detail"),
]
