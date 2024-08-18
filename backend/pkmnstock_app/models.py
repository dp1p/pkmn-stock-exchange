import requests
from django.db import models
from django.core import validators as v

# Create your models here.
class PkmnStock(models.Model):
    pokedex_id = models.IntegerField(unique=True) #this is here so now the admin must enter the pokedex no. of a pokemon to get valid information
    name = models.CharField(max_length=255, unique=True)
    # base_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    moves = models.JSONField(blank=True, null=True)
    #this will determine the base price of a pokemon
    what_type = models.JSONField(blank=True, null=True)
    base_stats = models.JSONField(blank=True, null=True)
    move_count = models.JSONField(blank=True, null=True)
    base_price = models.JSONField(blank=True, null=True)
    description = models.JSONField(blank=True, null=True)
    evolution_stages = models.JSONField(blank=True, null=True)
    price_history = models.JSONField(blank=True, null=True)



    def __str__(self):  
        return f"{self.name} (Pokedex ID: {self.pokedex_id})"