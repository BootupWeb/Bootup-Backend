from django.db import models

from .credentials import Credentials

class Profiles(models.Model):
    user = models.ForiegnKey(Credentials, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=22)
    last_name = models.CharField(max_length=22)
    gender = models.SmallIntegerField(default='') # 1=Male, 2=Female, 3=Other
    phone = models.CharField(max_length=13, default='000-000-0000')
    city = models.CharField(max_length=22)
    state = models.CharField(max_length=4)
    day = models.SmallIntegerField(default='01')
    month = models.SmallIntegerField(default='01')
    year = models.SmallIntegerField(default='1920')
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.username
