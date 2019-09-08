# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
CITY_CHOICES = (
    ('toronto', 'toronto'),
    ('edmonton', 'edmonton'),
    ('new york', 'new york'),
    ('montreal', 'montreal'),
    ('ottawa', 'ottawa'),
)

FOOD_CATEGORIES = (
    ('french', 'french'),
    ('indian', 'indian'),
)

class DropDownModel(models.Model):
    cities = models.CharField(max_length=6, choices=CITY_CHOICES, default='green')
    food_categories = models.CharField(max_length=6, choices=FOOD_CATEGORIES, default='orange')

class ParsedData(models.Model):
    business_id = models.TextField(primary_key=True, blank=False)
    name = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    stars = models.TextField(blank=True, null=True)
    review_count = models.TextField(blank=True, null=True)
    categories = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parsed_data'