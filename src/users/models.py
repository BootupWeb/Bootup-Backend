from django.db import models

class Credentials(models.Model):
    username = models.CharField(max_length=22),
    password = models.CharField(max_length=22),
    email = models.EmailField(max_length=100),
    token = models.CharField(max_length=225)

    def __str__(self):
        return self.username


class Profiles(models.Model):
    user = models.ForeignKey(Credentials, on_delete=models.CASCADE)
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

class Roles(models.Model):
    user = models.ForeignKey(Credentials, on_delete=models.CASCADE)
    type = models.CharField(max_length=9)
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=30)
    commitment = models.TextField(null=True)
    since_month = models.IntegerField()
    since_year = models.IntegerField()
    portfolio = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.type
