from django.db import models

from posts.models import Post


class PlaceTag(models.Model):

    place_name = models.CharField(
            max_length=20,
            )

    post_set = models.ManyToManyField(Post)

    def __str__(self):
        return self.place_name
