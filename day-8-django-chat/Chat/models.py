from django.db import models
from django.urls import reverse


class Chat(models.Model):
    message = models.TextField()
    sender = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.message
