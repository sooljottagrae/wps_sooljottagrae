from django.db import models


class Follow(models.Model):
    follower = models.ForeignKey(
            "User",
            related_name="+",
            )
    followee = models.ForeignKey(
            "AlcoholTag",
            related_name="+",
            )
