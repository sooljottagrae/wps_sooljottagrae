import datetime
import os

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

from users.models import User

def set_filename_format(now, instance, filename):
    return "{nickname}-{date}-{microsecond}{extension}".format(
            nickname=instance.user.email,
            date=str(now.date()),
            microsecond=now.microsecond,
            extension=os.path.splitext(filename)[1],
            )

def user_directory_path(instance, filename):
    now = datetime.datetime.now()
    
    path = "images/{year}/{month}/{day}/{email}/{filename}".format(
            year=now.year,
            month=now.month,
            day=now.day,
            email=instance.user.email,
            filename=set_filename_format(now, instance, filename),
            )

    return path


class PostManager(models.Manager):
    def public(self):
        return self.filter(is_public=True)


class Post(models.Model):

    objects = PostManager()
    user = models.ForeignKey(User)

    post_id = models.CharField(
        max_length=20,
    )

    title = models.CharField(
        max_length=30,
    )

    content = models.CharField(
        max_length=300,
    )

    image = models.ImageField(
        upload_to=user_directory_path,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_public = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "posts:detail",
            kwargs={
                "pk": self.id,
            }
        )

    def get_update_url(self):
        return reverse(
            "posts:update",
            kwargs={
                "post_id": self.id,
            }
        )

    def get_image_url(self):
        if self.image:
            return self.image.url
        return "http://placehold.it/300x200"
