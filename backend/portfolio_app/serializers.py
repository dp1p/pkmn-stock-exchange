from rest_framework import serializers
from pkmnstock_app.models import PkmnStock
from .models import Portfolio, PkmnPortfolio

class PkmnPortfolio(serializers.ModelSerializer): #creating our own pkmnstock serializer to display certain info when calling the pkmnstock model
    class Meta:
        model = PkmnStock
        fields = ['name', 'base_price', 'shares_purchased']

class PortfolioSerializer(serializers.ModelSerializer):
    pokemon = PkmnPortfolio(many=True, read_only=True, required=False)

    class Meta:
        model = Portfolio
        fields = ['user', 'buying_power', 'total_portfolio']