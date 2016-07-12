from django.conf.urls import url

from apis.views import *

urlpatterns = [
        url(r'^$', UserListAPIView.as_view(), name="list"),
        url(r'^login/$', UserLoginAPIView.as_view(), name="login"),
        url(r'^signup/$', UserCreateAPIView.as_view(), name="signup"),
        url(r'^(?P<pk>\d+)/$', UserDetailAPIView.as_view(), name="detail"),
]
