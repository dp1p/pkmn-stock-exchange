from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from .models import PkmnStock
from .serializers import PkmnStockSerializer #to see json information from the model
from user_app.views import TokenReq #if there is a specific view only a user can see (like how many shares)

# Create your views here.
class All_pokemon(APIView):
    def get(self, request):
        all_pkmn = PkmnStock.objects.all()
        serializer = PkmnStockSerializer(all_pkmn, many=True)
        return Response(serializer.data, status=HTTP_200_OK)