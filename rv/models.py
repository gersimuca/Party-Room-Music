from django.db import models


class PostRV(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(null=True)