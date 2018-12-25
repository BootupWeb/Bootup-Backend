from django.db import models

class Credentials(models.Model):
    username = models.CharField(max_length=22),
    password = models.CharField(max_length=22),
    email = models.EmailField(max_length=100),
    token = models.CharField(max_length=225)

    def __str__(self):
        return self.username
