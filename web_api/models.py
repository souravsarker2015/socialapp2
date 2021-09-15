from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    image = models.ImageField(upload_to='upload/user', blank=True)

    class Meta:
        db_table = "model_users"


class Status(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    text = models.TextField()
    address = models.CharField(max_length=100, null=True)
    share = models.IntegerField(default=0)
    tags = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "model_status"


class StatusImages(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='upload/status', blank=True)

    class Meta:
        db_table = "model_status_images"


class StatusLike(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, default=None, related_name='likes', on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "model_status_like"
