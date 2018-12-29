from django.db import models

from campaign.models import Detail
from users.models import Investor

class Chat(models.Model):
    campaign = models.ForeignKey(Detail, on_delete=models.CASCADE)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    subject = models.CharField(max_length=32, default='random message')

    def __str__(self):
        return 'Chat: ' + self.campaign.name + ' - ' + self.investor
