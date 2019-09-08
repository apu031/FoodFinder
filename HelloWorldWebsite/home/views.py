# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views import generic
from .models import Counter
from .mycharts import MyBarChartDrawing

# Create your views here.
class Home(generic.DetailView):
    model = Counter
    template_name = "home/index.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        return redirect('homepage')

def getBarChart(request):
    # if (request.GET.get('category') is not None):
    #     context['image_url'] = '/bar'

    d = MyBarChartDrawing()
    binaryStuff = d.asString('gif')
    return HttpResponse(binaryStuff, '/image/gif')