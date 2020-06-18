"""HelloWorldWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.food, name='food')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='food')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='homepage'),
    path('barchart.png', views.get_bar_chart, name='getbarchart'),
    path('fetch_city', views.fetch_city, name='fetch_city'),
    path('search/', views.search, name='search'),
    path('csv/', views.getfile, name='csv'),
]
