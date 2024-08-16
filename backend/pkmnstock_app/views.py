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
        #this will first check if this pokemon is our local database...
        if isinstance(pokemon_id, int): #if the user enters is a digit num
            try:
                pokemon = PkmnStock.objects.get(pokedex_id=pokemon_id) #grab the pokedex num
            except PkmnStock.DoesNotExist: #else if the pkmn is NOT in our local database
                pokemon = None
        else: #the instance is str
            try:
                pokemon = PkmnStock.objects.get(name=pokemon_id.title())
            except PkmnStock.DoesNotExist:
                pokemon = None
        
        
        # now we fetch data from the OUTSIDE database: PokeAPI
        if not pokemon: #if pkmn is set to None
            data = fetch_pokemon_data(pokemon_id)  #calls the fetch_pokemon_data func in services.py
            if not isinstance(data, dict): #checks the type of data, if it is not json/dict, then return response
                return Response({'error': 'No data available from PokeAPI or it is a legendary / mythical Pokemon.'}, status=HTTP_404_NOT_FOUND)
            
            pokemon = PkmnStock.objects.create(
                name = data.get('name').title(), # we are grabbing the name from the data
                pokedex_id = data.get('pokedex_id'),  #we are grabbing the pokedex id from the data
                description = data.get('description'),
                what_type = data.get('types'),
                base_stats = data.get('base_stats'),
                move_count = data.get('move_count'),
                moves = data.get('moves'),
                base_price = data.get('base_price'),
                evolution_stages = data.get('evolution_stages')
            )

        # serialize the Pokemon data and return the response into json format
        serializer = PkmnStockSerializer(pokemon)
        return Response(serializer.data, status=HTTP_200_OK)