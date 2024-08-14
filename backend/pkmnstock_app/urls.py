# import register converter to create new param types in URL patterns
from django.urls import path, register_converter
# import our converter class to utilize as a parameter 
from .converters import IntOrStrConverter
from .views import All_pokemon, Pokemon_info

# to use this custom converter in a URL pattern
register_converter(IntOrStrConverter, 'int_or_str')


#api/v1/pkmn/...
urlpatterns = [
    path('allpkmn/', All_pokemon.as_view()),
    path('<int_or_str:pokemon_id>/', Pokemon_info.as_view()), #whether or not if id is int or str
]