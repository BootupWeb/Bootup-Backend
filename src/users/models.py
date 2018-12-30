from django.db import models

from campaign.models import Detail

from .choices import MONTH_CHOICES, ROLE_CHOICES, GENDER_CHOICES

class Credential(models.Model):
    username = models.CharField(max_length=22)
    password = models.CharField(max_length=22)
    email = models.EmailField(max_length=100)
    token = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.ForeignKey(Credential, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=22)
    last_name = models.CharField(max_length=22)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES) # 1=Male, 2=Female, 3=Other
    phone = models.CharField(max_length=13, default='000-000-0000')
    city = models.CharField(max_length=22)
    state = models.CharField(max_length=4)
    day = models.SmallIntegerField(default='01')
    month = models.SmallIntegerField(choices=MONTH_CHOICES, default="January")
    year = models.SmallIntegerField(default='1920')
    website = models.URLField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

class Founder(models.Model):
    user = models.ForeignKey(Credential, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Detail, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=30)
    commitment = models.TextField(null=True)
    since_month = models.CharField(max_length=15, choices=MONTH_CHOICES)
    since_year = models.IntegerField()
    portfolio = models.CharField(max_length=200)
    relation = models.TextField()
    known = models.IntegerField()
    verified = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + '-' + self.campaign.name

class Investor(models.Model):
    user = models.ForeignKey(Credential, on_delete=models.CASCADE)
    company = models.CharField(max_length=32)
    position = models.CharField(max_length=45)
    since_month = models.CharField(max_length=15, choices=MONTH_CHOICES)
    since_year = models.IntegerField()
    summary = models.TextField()
    top_investment = models.CharField(max_length=22)
    current_investments = models.IntegerField()
    portfolio_link = models.URLField()
    portfolio_file = models.URLField()
    verified = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' - ' + self.position
