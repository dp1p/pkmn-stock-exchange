from rest_framework import serializers
from .models import PkmnStock
#converts psql / django model to json readable

class PkmnStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = PkmnStock
        fields = ['name', 'pokedex_id', 'what_type', 'description', 'base_stats', 'base_price', 'move_count', 'evolution_stages', 'price_history',  ]
        #'moves'