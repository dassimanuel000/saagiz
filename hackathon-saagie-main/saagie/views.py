from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from string import Template
import requests
from django.template import RequestContext


def restore(request):
    return render('audit.html')


def audit(request):
    return render(request, "hackathon/home.html")

def home(request):
    return render(request, "hackathon/index.html")
