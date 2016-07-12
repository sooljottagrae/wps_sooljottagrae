from django.views.generic import View
from django.http.response import HttpResponse
from django.conf import settings
from django.db import models


class Meetup(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)


class PostListAPIView(View):
    pass
