from django.db import models


class Tag(models.Model):

    class Meta:
        verbose_name = 'Category'
        ordering = ['name']

    name = models.CharField(
            verbose_name = 'Category',
            max_length=20,
            )

    def __str__(self):
        return self.name
