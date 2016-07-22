from django.db import models
from django.core.urlresolvers import reverse

from users.models import MyUser


class PostManager(models.Manager):
    def public(self):
        return self.filter(is_public=True)


class Post(models.Model):

    objects = PostManager()
    user = models.ForeignKey(MyUser) 

    content = models.CharField(
        max_length=300,
    )

    image = models.ImageField(
        blank=True,
        null=True,
    )

    location = models.CharField(
        blank=True,
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
