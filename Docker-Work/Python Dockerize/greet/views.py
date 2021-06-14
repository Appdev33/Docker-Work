from django.shortcuts import render
# from django import HttpResponse
from django.shortcuts import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse("hello world")
