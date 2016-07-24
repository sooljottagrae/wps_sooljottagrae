from django.db import models
from django.core.urlresolvers import reverse
from users.models import User


class Comment(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey("Post")

    content = models.TextField()

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse(
            "posts:detail",
            kwargs={
                "pk": self.post.id,
            },
        ) + "#comment-" + str(self.id)

    def get_absolute_api_url(self):
        return reverse(
            "apis:comments:detail",
            kwargs={
                "id": self.id,
            },
        )
