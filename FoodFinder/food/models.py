# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
CITY_CHOICES = (
    ('Toronto', 'Toronto'),
)


class DropDownModel(models.Model):
    cities = models.CharField(max_length=50, choices=CITY_CHOICES, default='green')


class ParsedData(models.Model):
    business_id = models.TextField(primary_key=True, blank=False)
    name = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    stars = models.TextField(blank=True, null=True)
    review_count = models.TextField(blank=True, null=True)
    categories = models.TextField(blank=True, null=True)
