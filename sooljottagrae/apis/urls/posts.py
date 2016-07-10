from django.conf.urls import url

from apis.views import *

urlpatterns = [
        url(r'$', PostListAPIView.as_view(), name="list"),
        url(r'create/$', PostCreateAPIView.as_view(), name="create"),
        url(r'(?P<pk>\w+)/$', PostDetailAPIView.as_view(), name="detail"),
        url(r'(?P<pk>\w+)/edit/$', PostUpdateAPIView.as_view(), name="edit"),
        url(r'(?P<pk>\w+)/delete/$', PostDeleteAPIView.as_view(), name="delete"),
        ]
