from django.db import models
from django.conf import settings
from django_cryptography.fields import encrypt
# app models
from market.model.market import Market


class KeyManager(models.Manager):
    pass


class Key(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='keys')
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='keys')
    api_key = encrypt(models.CharField(max_length=500, blank=True, null=True))
    api_secret = encrypt(models.CharField(max_length=500, blank=True, null=True))

    objects = KeyManager()

    def __str__(self):
        return f'{self.user} - {self.market}'