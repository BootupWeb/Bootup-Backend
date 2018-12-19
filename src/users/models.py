from django.db import models

class Credentials(models.Model):
  username = models.CharField(max_length=22, null=false)
  password = models.CharField(max_length=200, null=false)
  email = models.CharField(max_length=66, null=false)
  