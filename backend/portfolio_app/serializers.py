from rest_framework import serializers
from pkmnstock_app.models import PkmnStock
from .models import Portfolio, PkmnPortfolio

class PkmnPortfolioSerializer(serializers.ModelSerializer): #creating our own pkmnstock serializer to display certain info when calling the pkmnstock model
    pokemon = serializers.CharField(source='pokemon.name')  # will grab the 'name' from the pkmnstock model in the class 'meta'
    pokedex_id = serializers.IntegerField(source='pokemon.pokedex_id')
    price_per_share = serializers.DecimalField(source='pokemon.base_price', max_digits=12, decimal_places=2) # will grab the 'price' of the pkmn name from the pkmnstock model in the class 'meta'

    class Meta:
        model = PkmnPortfolio #uses the model 'pkmnportfolio' because we want to use these specfic field
        fields = ['pokemon', 'pokedex_id', 'shares', 'price_per_share', 'total_price', 'purchase_date']

class PortfolioSerializer(serializers.ModelSerializer):
    pokemon = PkmnPortfolioSerializer(many=True, read_only=True, source='pkmn_in_portfolio')

    class Meta:
        model = Portfolio
        fields = ['user', 'buying_power', 'total_portfolio', 'pokemon']


