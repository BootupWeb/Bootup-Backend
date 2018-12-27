from django.db import models

FINANCIAL = 'Financial'
GREEN_ENERGY = 'Green Energy'

CATEGORY_CHOICES = (
    (FINANCIAL, 'financial'),
    (GREEN_ENERGY, 'green energy'),
)

class Detail(models.Model):
    name = models.CharField(max_length=32)
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES, default=FINANCIAL)
    sub_category = models.CharField(max_length=32) # add choices
    established = models.SmallIntegerField()
    url = models.URLField(max_length=200)
    demo = models.URLField(max_length=200)
    video = models.URLField(max_length=200)
    location_city = models.CharField(max_length=32)
    location_state = models.CharField(max_length=22)
    phone = models.CharField(max_length=13)
    progress = models.CharField(max_length=12)
    status = models.CharField(max_length=12)

    def __str__(self):
        return self.name
