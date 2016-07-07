from django.conf.urls import url

from posts.views import *


urlpatterns = [
    url(r'new/$', PostCreateFormView.as_view(), name="create"),
    url(r'confirm/$', PostCreateConfirmFormView.as_view(), name="confirm"),
]
