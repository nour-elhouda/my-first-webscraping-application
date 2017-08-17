# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
import urllib2
from bs4 import BeautifulSoup
from django.core.files import File
from .models import Lien
import csv, math
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm

def liste(request):
	return render(request, 'scraping/liste.html')

def scrip(my_url,filename) :
	page = urllib2.urlopen(my_url)
	page_html = page.read()
	page.close()

	#html parsing
	soup = BeautifulSoup(page_html, "html.parser")
	#grabs each item
	containers = soup.findAll("tr", {"class" : "Tableau1"})

	f = open(filename, 'w')
	headers = "region, nature, prix, date\n"
	#headers = "region\n"
	f.write(headers)

	for container in containers:
		tregion=container.find("a")
		region = tregion.text
		
		tnature= container.find("td" , {"style" : "CURSOR:pointer;"})
		nature = tnature.text.strip() 
		#strip() removes special caracters 
		
		tprix= container.find("td" , {"style" : "CURSOR:pointer;text-align: right;"})
		prix = tprix.text.strip()
		
		tdate=container.find_all("td" ,attrs= {"style" : "CURSOR:pointer;"})[2]
		date = tdate.text.strip()
	
			
		f.write(region +"," + nature + ","+ prix + "," + date +"\n")
	f.close()
	
def csvpars(t,f):
	with open(t) as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',')
		writer = open(f, 'w')
		writer.write('<center>')
		writer.write('<table class="table table-bordered">')
		for row in reader:
			writer.write('<tr>')
			for fn in reader.fieldnames:
				writer.write('<td>{}</td>'.format(row[fn]))
			writer.write('</tr>')
		writer.write('</table>')
		writer.write('</center>')
		
def test1(request):
	my_url= 'http://www.tunisie-annonce.com/AnnoncesImmobilier.asp'
	#opening up connection
	filename = "scraping/templates/scraping/tuniannonce.csv"
	file="scraping/templates/scraping/t2.html"
	scrip(my_url, filename)
	csvpars(filename,file)
	return render(request, 'scraping/test.html')
