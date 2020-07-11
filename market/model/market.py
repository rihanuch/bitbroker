from django.db import models
from django.conf import settings
from django_cryptography.fields import encrypt


class MarketManager(models.Manager):
    pass


class Market(models.Model):

    name = models.CharField(max_length=50)

    objects = MarketManager()

    def __str__(self):
        return self.name