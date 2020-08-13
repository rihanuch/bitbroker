from django.db import models
from django.utils import timezone
from django.conf import settings


class Message(models.Model):
    update_id = models.IntegerField(unique=True)
    text = models.TextField(max_length=4096)
    date = models.DateTimeField(default=timezone.now)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f'{self.text}'
