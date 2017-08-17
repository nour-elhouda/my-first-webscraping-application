from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from scraping.models import Lien
from django.contrib.auth.views import login
from django.shortcuts import get_object_or_404, render

urlpatterns = [
	url(r'^/$' , ListView.as_view(queryset=Lien.objects.all(), template_name="scraping/liste.html")),
	url(r'^/1$', views.test1, name='test1'),
	url(r'^/login/$', login, {'template_name': 'scraping/registration.html'})
]