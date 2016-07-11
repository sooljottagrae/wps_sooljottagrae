from django.conf.urls import url

from api.lists import *


urlpatterns = [
    url(r'^api/$', PostListAPIView.as_view(), name="list"),
]
