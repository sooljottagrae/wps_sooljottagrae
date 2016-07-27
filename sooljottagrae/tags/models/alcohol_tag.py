from django.db import models
from django.core.urlresolvers import reverse

from posts.models import Post
from users.models import User


class AlcoholTag(models.Model):

    alcohol_name = models.CharField(
            max_length=20,
            )

    post_set = models.ManyToManyField(Post)
    user_set = models.ManyToManyField(User)

    @property
    def full_name(self):
        return "#{alcohol_name}".format(alcohol_name=self.alcohol_name)

    def __str__(self):
        return self.full_name

    def get_absolute_api_url(self):
        return reverse(
            "apis:tags:alcohol-detail",
            kwargs={
                "pk": self.id,
            },
        )
