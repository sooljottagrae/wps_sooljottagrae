from django.conf.urls import url

from rest_framework_jwt.views import verify_jwt_token
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
        url(r'^verify/$', verify_jwt_token),
        url(r'^refresh/$', refresh_jwt_token),
]
