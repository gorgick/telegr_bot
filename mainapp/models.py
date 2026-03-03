from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Owner(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(blank=True, null=True)


class Notification(models.Model):
    user = models.ForeignKey(
        Owner, on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
