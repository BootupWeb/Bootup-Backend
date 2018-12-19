from django.db import models


class Credentials(models.Model):
    username = models.CharField(max_length=22)
    password = models.EmailField(max_length=200)
    email = models.CharField(max_length=66)

    def __str__(self):
        return self.username
