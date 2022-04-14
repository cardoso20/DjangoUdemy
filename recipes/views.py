from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html') #global/home.html chama o template base

def contact(request):
    return HttpResponse('contact')

def about(request):
    return HttpResponse('about')