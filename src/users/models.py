from django.db import models
from django.contrib.auth.models import User

from campaign.models import Detail

from .choices import MONTH_CHOICES, ROLE_CHOICES, GENDER_CHOICES

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=22)
    state = models.CharField(max_length=4)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES) # 1=Male, 2=Female, 3=Other
    phone = models.CharField(max_length=13, default='000-000-0000')
    day = models.SmallIntegerField(default='01')
    month = models.CharField(max_length=22, choices=MONTH_CHOICES, default="January")
    year = models.SmallIntegerField(default='1920')
    website = models.URLField(max_length=200)
    type = models.CharField(max_length=2, default='F')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username  + ' - ' + self.type

class Role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    campagin = models.ForeignKey(Detail, on_delete=models.CASCADE, null=True)
    firm = models.CharField(max_length=44)
    position = models.CharField(max_length=44)
    summary = models.TextField()
    since_month = models.CharField(max_length=22, choices=MONTH_CHOICES, default='January')
    since_year = models.SmallIntegerField()
    portfolio_url = models.URLField()
    current_inv = models.IntegerField()
    top_inv = models.CharField(max_length=44)
    varified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + ' - ' + self.position
