from django.conf.urls import url

from posts.views import *


urlpatterns = [
        url(r'^$', PostListView.as_view(), name="list"),
        url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name="detail"),
        url(r'^new/$', PostNewView.as_view(), name="new"),
        url(r'^create/$', PostCreateView.as_view(), name="create"),
        url(r'^(?P<post_id>\d+)/edit/$', edit, name="edit"),
        url(r'^(?P<post_id>\d+)/update/$', update, name="update"),
        url(r'^(?P<post_id>\d+)/delete/$', delete, name="delete"),
]
