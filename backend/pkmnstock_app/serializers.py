from rest_framework import serializers
from .models import PkmnStock
#converts psql / django model to json readable

class PkmnStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = PkmnStock
        fields = ['name', 'details']