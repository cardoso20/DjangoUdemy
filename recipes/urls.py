from django.urls import path
from recipes.views import home, about, contact

urlpatterns = [
    path('', home),
    path('contact/', contact),
    path('about/', about),
]
