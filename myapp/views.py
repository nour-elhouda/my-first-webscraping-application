# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'myapp/home.html')

def contact(request):
	return render(request, 'myapp/basic.html', {'content':['contact me', 'ayari.nourelhouda@gmail.com']})
	