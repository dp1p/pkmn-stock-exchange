from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from .models import PkmnStock
from .serializers import PkmnStockSerializer #to see json information from the model
from user_app.views import TokenReq #if there is a specific view only a user can see (like how many shares)
from .services import fetch_pokemon_data

# Create your views here.

#view all pokemon
class All_pokemon(APIView):
    def get(self, request):
        all_pkmn = PkmnStock.objects.all()
        serializer = PkmnStockSerializer(all_pkmn, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

#view pokemon info REQUIRES LOGIN
class Pokemon_info(TokenReq):
    def get(self, request, pokemon_id):
        if isinstance(pokemon_id, int): #if the user enters is a digit num
            # Assuming identifier is a valid ID if it's all digits
            pokemon = get_object_or_404(PkmnStock, pk=pokemon_id)
        else:
            # Treat identifier as a name if it's not all digits
            pokemon = get_object_or_404(PkmnStock, name=pokemon_id.title())
        
        # Fetch data from PokeAPI
        data = fetch_pokemon_data(pokemon_id)  # This function should handle both names and IDs
        if data:
            pokemon.details = data  # Update the details directly on the model instance
            pokemon.save()  # Save the model instance to persist changes
        else:
            return Response({'error': 'No data available from PokeAPI'}, status=HTTP_404_NOT_FOUND) #this is kind of misleading because it will only display pkmn info that are in our database

        # Serialize the Pokemon data and return the response
        serializer = PkmnStockSerializer(pokemon)
        return Response(serializer.data, status=HTTP_200_OK)