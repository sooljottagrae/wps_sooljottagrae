from django.db import models

from users.models import User


class Comment(models.model):
    user = models.ForeignKey(User)
    post = models.foreignKey("Post")

    content = models.TextField()

    created_at = models.DataTimeField(auto_now_add=True)
    updated_at = models.DataTimeField(auto_now=True)

    def __str__(self):
        return self.content
