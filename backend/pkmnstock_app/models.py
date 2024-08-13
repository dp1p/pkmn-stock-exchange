import requests
from django.db import models
from django.core import validators as v

#this model will grab the base stats, convert it to a price
#this will also store all the price action

# def pkmn_base_stats(pokemon_name):
#     url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/"

# Create your models here.
class PkmnStock(models.Model):
    name = models.CharField(max_length=255, unique=True)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):  
        return self.name
