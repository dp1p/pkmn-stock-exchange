from django.urls import path
from .views import All_pokemon

urlpatterns = [
    path('allpkmn', All_pokemon.as_view())
]