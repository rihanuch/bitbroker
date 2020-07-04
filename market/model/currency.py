from django.db import models
from django.conf import settings


class Currency(models.Model):

    name = models.CharField(max_length=50, unique=True)
    symbol = models.CharField(max_length=5)

    def __str__(self):
        return self.symbol