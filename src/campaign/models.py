from django.db import models

from .choices import CATEGORY_CHOICES, PLATFORM_CHOICES, PROGRESS_CHOICES, SIZE_CHOICES

class Detail(models.Model):
    name = models.CharField(max_length=32)
    slug = models.CharField(max_length=225, default="describe product in 225 characters")
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES)
    platform = models.CharField(max_length=22, choices=PLATFORM_CHOICES)
    established = models.SmallIntegerField()
    url = models.URLField(max_length=200)
    video = models.URLField(max_length=200)
    location_city = models.CharField(max_length=32)
    location_state = models.CharField(max_length=22)
    progress = models.CharField(max_length=22, choices=PROGRESS_CHOICES)
    status = models.CharField(max_length=22, choices=SIZE_CHOICES)
    equity = models.DecimalField(max_digits=5, decimal_places=2, default=33.33)
    amount = models.DecimalField(max_digits=17, decimal_places=2, default=1000.00)
    valuation = models.DecimalField(max_digits=17, decimal_places=2, default=3333.33)
    featured_images = models.ImageField(upload_to='featured_images/', default="http://via.placeholder.com/300x300")
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Story(models.Model):
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)
    product = models.TextField()
    far_along = models.TextField()
    users_count = models.TextField()
    new = models.TextField()
    different = models.TextField()
    competitors = models.TextField()
    user_aquisition = models.TextField()
    monetization = models.TextField()
    pick_project = models.TextField()
    money_use = models.TextField()
    future_six = models.TextField()
    future_one = models.TextField()
    future_two = models.TextField()
    future_three = models.TextField()
    other_projects = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.details.name + ' - ' + self.product

class Update(models.Model):
    campaign = models.ForeignKey(Detail, on_delete=models.CASCADE)
    message = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.campaign.name + ' update'
