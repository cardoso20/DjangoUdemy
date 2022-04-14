from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('home')

def contact(request):
    return HttpResponse('contact')

def about(request):
    return HttpResponse('about')