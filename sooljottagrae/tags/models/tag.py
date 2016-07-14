from django.db import models


class Tag(models.Model):

    place = models.CharField(
            max_length=20,
            )
    food = models.CharField(
            max_length=20,
            )
    drink = models.CharField(
            max_length=20,
            )


