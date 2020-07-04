from django.db import models
from django.conf import settings
from django_cryptography.fields import encrypt


class Market(models.Model):

    name = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.name