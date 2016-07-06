from django.conf.urls import url

from apis.views import *
urlpatterns = [
        url(r'^posts/$', PostListAPIView.as_view(), name="postlist"),
        url(r'^posts/(?P<pk>\w+)/$', PostDetailAPIView.as_view(), name="postdetail"),

        url(r'^users/$', UserListAPIView.as_view(), name="userlist"), 
        url(r'^users/(?P<pk>\w+)/$',UserDetailAPIView.as_view(), name="userdetail"),
        ]
