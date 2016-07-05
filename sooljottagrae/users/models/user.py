from django.contrib.auth.models import User as AbstractUser
from django.db import models
from django.db.models.signals import post_save

from django.dispatch import receiver


class User(AbstractUser):
    phonenumber = models.CharField(
        max_length=16,
        blank=True,
        null=True,
    )


class UserProfile(models.Model):
    user = models.OneToOneField(User)


@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
