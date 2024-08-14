import requests
from django.db import models
from django.core import validators as v

#we will use .services to grab the pokemon from the api
from .services import fetch_pokemon_data

# Create your models here.
class PkmnStock(models.Model):
    name = models.CharField(max_length=255)
    # base_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    details = models.JSONField(blank=True, null=True)

    def __str__(self):  
        return self.name