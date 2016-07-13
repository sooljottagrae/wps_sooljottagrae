from django.db import models
from users.models import User


class Post(models.Model):

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
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
