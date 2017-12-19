from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    email = models.EmailField()

    def __str__(self):
        return self.name
