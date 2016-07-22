from django.conf.urls import url, include

from rest_framework_jwt.views import obtain_jwt_token

from apis.views import *

urlpatterns = [
        url(r'^$', UserListAPIView.as_view(), name="list"),
        # url(r'^login/$', UserLoginAPIView.as_view(), name="login"),
        url(r'^login/$', obtain_jwt_token),
        url(r'^signup/$', UserCreateAPIView.as_view(), name="signup"),
        url(r'^(?P<pk>\d+)/$', UserDetailAPIView.as_view(), name="detail"),

        url(r'^auth/', include('rest_framework_social_oauth2.urls')),
]
