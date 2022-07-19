from re import A
from django.contrib import admin
from models import Recipe, Category

class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)