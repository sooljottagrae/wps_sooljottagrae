from django.db import models
from django.core.urlresolvers import reverse

from posts.models import Post
from users.models import User


class FoodTag(models.Model):

    food_name = models.CharField(
            max_length=20,
            )

    post_set = models.ManyToManyField(Post)
    user_set = models.ManyToManyField(User)

    @property
    def full_name(self):
        return "#{food_name}".format(food_name=self.food_name)

    def __str__(self):
        return self.full_name

    def get_absolute_api_url(self):
        return reverse(
            "apis:tags:food-detail",
            kwargs={
                "pk": self.id,
            },
        )
