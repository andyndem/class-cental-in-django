# from django.shortcuts import render
# from django.http import HttpResponse
# from bs4 import BeautifulSoup
# import requests
from django.shortcuts import render, redirect



def index(request):
  return render(request, "scrape/index.html")

def stanford(request):
  return render(request, "scrape/stanford.html")

def coursera(request):
  return render(request, "scrape/coursera.html")

def havard(request):
  return render(request, "scrape/havard.html")
