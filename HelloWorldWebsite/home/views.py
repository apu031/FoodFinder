# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views import generic
from .mycharts import MyBarChartDrawing
from django.views.generic import CreateView
from .models import DropDownModel, ParsedData
from .forms import DropDownModelForm
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.db import models

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

def fetchCity(request):
    city = request.POST.get('cities')
    return redirect('/?city='+city)

def search(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            # total = ParsedData.objects.count()
            queried_data = ParsedData.objects. \
                values('city'). \
                annotate(
                type_count=
                models.Sum(models.F('stars') * models.F('review_count'), output_field=models.IntegerField())
                / models.Count('business_id')
            ) \
                .filter(categories__contains=search_id) \
                .order_by('-type_count')
            # context = {'total' : total, 'p':queried_data}
            # return render(request, 'polls/index.html', context)
            diction = {}
            for data in queried_data:
                diction[data['city']] = data['type_count']
            # Data for plotting
            fig = plt.figure()
            ax = plt.gca()
            x = list(diction.keys())
            y = list(diction.values())
            ax.bar(x, y, color='gray')

            ax.set(xlabel='Cities', ylabel='Score',
                   title='Ranking Cities Based on ' + search_id + " Food")
            # ax.grid()
            response = HttpResponse(content_type='image/png')

            canvas = FigureCanvasAgg(fig)
            canvas.print_jpg(response)
            return response
        except:
            return HttpResponse("Invalid Search.")

    else:
        return render(request, 'polls/form.html')
