from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blogger(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=10, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    blogger = models.ForeignKey(Blogger, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50, null=True)
    body = models.CharField(max_length=10000000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
