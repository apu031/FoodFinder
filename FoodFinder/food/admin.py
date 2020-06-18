# -*- coding: utf-8 -*-

from django.contrib import admin

from food.models import DropDownModel, ParsedData


class DropDownModelAdmin(admin.ModelAdmin):
    model = DropDownModel
    list_display = ['id', 'cities']

class ParsedDataAdmin(admin.ModelAdmin):
    model = ParsedData
    list_display = ['business_id', 'name', 'city', 'stars', 'review_count', 'categories']


admin.site.register(DropDownModel, DropDownModelAdmin)
admin.site.register(ParsedData, ParsedDataAdmin)