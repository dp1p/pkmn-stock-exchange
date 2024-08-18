from rest_framework import serializers
from pkmnstock_app.models import PkmnStock

class PkmnWatchlistSerializer(serializers.ModelSerializer): #creating a serializer using the 'pkmnstock' model to display SPECIFIC info
    class Meta:
        model = PkmnStock #use the 'PkmnStock' model
        fields = ['name', 'base_price'] #and display certain info

class WatchlistSerializer(serializers.ModelSerializer):
    pokemon = PkmnWatchlistSerializer(many=True) 

    #specify what we want to return in here
    class Meta:
        model = PkmnStock #specify what model we want to grab
        fields = ['name', 'pokemon'] #get the name of our watch, and return what pokemon is in it



