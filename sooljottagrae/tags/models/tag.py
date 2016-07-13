from django.db import models

from posts.models import Post


class Tag(models.Model):

    name = models.CharField(
            max_length=20,
            )

    def __str__(self):
        return self.name
