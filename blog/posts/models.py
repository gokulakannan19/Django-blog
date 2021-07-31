from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50, null=True)
    body = models.CharField(max_length=10000000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
