# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import csv

import matplotlib.pyplot as plt
from django.db import models
from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView
from matplotlib.backends.backend_agg import FigureCanvasAgg

from .forms import DropDownModelForm
from .models import DropDownModel, ParsedData
from .mycharts import MyBarChartDrawing


def getfile(request):
    with open("food_places.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        count = 0
        for line in reader:
            if count != 0:
                # print(line[1], line[2], line[5], line[10], line[11], line[13])
                ParsedData.objects.create(
                    business_id=line[1],
                    name=line[2],
                    city=line[5],
                    stars=line[10],
                    review_count=line[11],
                    categories=line[13]
                )
            count += 1
            # print(count)
    return JsonResponse({
        'message': 'successfully uploaded',
    }, status=201)


# Create your views here.
class Home(CreateView):
    model = DropDownModel
    template_name = "home/index.html"
    form_class = DropDownModelForm


def get_bar_chart(request):
    d = MyBarChartDrawing()
    binary_stuff = d.asString('gif')
    return HttpResponse(binary_stuff, '/image/gif')


def fetch_city(request):
    city = request.POST.get('cities')
    print(city)
    unique_categories = set()
    categories = [query['categories'].split(', ') for query in
                  ParsedData.objects.values('categories').filter(city=city)]

    for category in categories:
        for cate in category:
            unique_categories.add(cate)

    print(unique_categories)
    # category = ['Chinese', 'Indian', 'Mexican', 'Canadian', 'Greek']

    cat_list = []
    for cate in unique_categories:
        cat_list.append((cate, ParsedData.objects.order_by().filter(city=city, categories__contains=cate).count()))

    cat_list = sorted(cat_list, key=lambda x: (-x[1], x[0]))[:5]

    # Data for plotting
    fig = plt.figure(num=None, figsize=(16, 12), facecolor='w', edgecolor='k')
    ax = plt.gca()
    x = list(item[0] for item in cat_list)
    y = list(item[1] for item in cat_list)
    ax.bar(x, y, color='gray')

    ax.set(xlabel='Food Type', ylabel='Number of Restuarant',
           title='Ranking Cuisine Based on ' + city + " Food")
    # ax.grid()
    response = HttpResponse(content_type='image/png')

    canvas = FigureCanvasAgg(fig)
    canvas.print_jpg(response)
    return response


def search(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)

        try:
            queried_data = ParsedData.objects.values('city').annotate(
                type_count=models.Sum(
                    models.F('stars') * models.F('review_count'),
                    output_field=models.IntegerField()
                ) / models.Count('business_id')).filter(categories__contains=search_id).order_by('-type_count')[:10]

            diction = {}
            for data in queried_data:
                diction[data['city']] = data['type_count']

            # Data for plotting
            fig = plt.figure(num=None, figsize=(16, 12), facecolor='w', edgecolor='k')
            ax = plt.gca()
            plt.xticks(rotation=45)
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
        except ValueError:
            return HttpResponse(str(ValueError) + "Invalid Search.")

    else:
        return HttpResponse("Invalid Post.")
