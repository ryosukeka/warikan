from django.conf import settings
from django.db import models
from django.utils import timezone

class Tracs(models.Model):
    payer = models.TextField()
    nonpayer = models.TextField()
    amount = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    item = models.TextField()

class Total(models.Model):
    repayer = models.TextField()
    reciever = models.TextField()
    total = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
