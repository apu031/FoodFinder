# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from .models import DropDownModel
from .forms import DropDownModelForm

class Home(CreateView):
    model = DropDownModel
    template_name = "home/index.html"
    form_class = DropDownModelForm
