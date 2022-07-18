from tkinter.tix import Tree
from django.shortcuts import render
from utils.recipes.factory import make_recipe

def home(request):
    return render(request, 'recipes/pages/home.html', context= {
        'recipes': [make_recipe() for _ in range(10)]
    }) #global/home.html chama o template base

def recipe(request, id):
    return render(request, 'recipes/pages/recipe.html', context= {
        'recipe': make_recipe(),
        'is_detail_page': True
    })