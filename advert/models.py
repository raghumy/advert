from django.db import models
from django.conf import settings


# Create your models here.


class Advertiser(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    credit_limit = models.IntegerField()