from rest_framework import serializers
from pkmnstock_app.models import PkmnStock

class WatchlistSerializer(serializers.ModelSerializer):
    pokemon = serializers.SerializerMethodField() 

    #specify what we want to return in here
    class Meta:
        model = PkmnStock #specify what model we want to grab
        fields = ['name', 'base_price']

    def get_pokemon(self, instance):
        #get a list of all the pkmn which our watchlist has
        pokemon = instance.pokemon.all()

        #turns the list of obj to list of dictionaries
        ser_pokemon = [{'name': p.name} for p in pokemon]

        return ser_pokemon




