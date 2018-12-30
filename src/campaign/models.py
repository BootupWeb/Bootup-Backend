from django.db import models

from .choices import CATEGORY_CHOICES, PLATFORM_CHOICES, PROGRESS_CHOICES, SIZE_CHOICES

class Detail(models.Model):
    name = models.CharField(max_length=32)
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES)
    #sub_category = models.CharField(max_length=32) # add choices
    platform = models.CharField(max_length=22, choices=PLATFORM_CHOICES)
    established = models.SmallIntegerField()
    url = models.URLField(max_length=200)
    demo = models.URLField(max_length=200)
    video = models.URLField(max_length=200)
    location_city = models.CharField(max_length=32)
    location_state = models.CharField(max_length=22)
    phone = models.CharField(max_length=13)
    progress = models.CharField(max_length=22, choices=PROGRESS_CHOICES)
    status = models.CharField(max_length=22, choices=SIZE_CHOICES)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Story(models.Model):
    details = models.ForeignKey(Detail, on_delete=models.CASCADE)
    slug = models.CharField(max_length=225)
    product = models.TextField()
    summary = models.TextField()
    pick_project = models.TextField()
    far_along = models.TextField()
    competitors = models.TextField()
    different = models.TextField()
    new = models.TextField()
    money_use = models.TextField()
    user_aquisition = models.TextField()
    monetization = models.TextField()
    users_count = models.TextField()
    equity_summary = models.TextField()
    future_six = models.TextField()
    future_one = models.TextField()
    future_two = models.TextField()
    future_three = models.TextField()
    other_projects = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.details.name + ' - ' + self.slug

class Update(models.Model):
    campaign = models.ForeignKey(Detail, on_delete=models.CASCADE)
    message = models.TextField()
    impact = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.campaign.name + ' update'
