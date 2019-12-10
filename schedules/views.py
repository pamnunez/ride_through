from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to RideThrough, your scheduling tool for SEPTA Regional Rail travel to/from outlying stations travelling through CC.")
