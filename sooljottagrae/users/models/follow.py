from django.db import models


class follow(models.Model):
    follower = models.ForeignKey(
            "User",
            related_name="+",
            )
    followee = models.FoereignKey(
            "AlcoholTag",
            related_name="+",
            )
