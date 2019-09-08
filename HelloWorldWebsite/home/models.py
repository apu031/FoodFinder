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

