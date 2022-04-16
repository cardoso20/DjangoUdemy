from django.shortcuts import render

def home(request):
    return render(request, 'recipes/pages/home.html') #global/home.html chama o template base