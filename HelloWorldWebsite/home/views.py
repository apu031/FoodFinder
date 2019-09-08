# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views import generic
from .mycharts import MyBarChartDrawing
from django.views.generic import CreateView
from .models import DropDownModel
from .forms import DropDownModelForm

# Create your views here.
class Home(CreateView):
    model = DropDownModel
    template_name = "home/index.html"
    form_class = DropDownModelForm
    
def getBarChart(request):
    # if (request.GET.get('category') is not None):
    #     context['image_url'] = '/bar'

    d = MyBarChartDrawing()
    binaryStuff = d.asString('gif')
    return HttpResponse(binaryStuff, '/image/gif')
