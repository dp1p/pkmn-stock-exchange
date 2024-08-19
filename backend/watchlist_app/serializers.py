from rest_framework import serializers
from pkmnstock_app.models import PkmnStock
from .models import Watchlist

class PkmnWatchlistSerializer(serializers.ModelSerializer):  #creating our own pkmnstock serializer to display certain info when calling the pkmnstock model
    class Meta:
        model = PkmnStock
        fields = ['name', 'base_price']

class WatchlistSerializer(serializers.ModelSerializer):
    pokemon = PkmnWatchlistSerializer(many=True, read_only=True, required=False)
    
    class Meta:
        model = Watchlist
        fields = ['name', 'pokemon']

    def create(self, validated_data): #creating a new watchlist to ensure that it is connected to the user (was geting a 'user_id' is null error without this)
        user = self.context['request'].user  #grab the currently authenticated user from the 'request' #'context' allows serializers to acces the information of .user
        watchlist = Watchlist.objects.create(user=user, **validated_data) #create watchlist with the user_id tied to the watchlist with validated data
        return watchlist