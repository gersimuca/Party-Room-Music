from django.db import models


class PostTV(models.Model):
    name = models.CharField(max_length=100)