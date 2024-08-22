from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from .models import PkmnStock
from .serializers import PkmnStockSerializer #to see json information from the model
from user_app.views import TokenReq #if there is a specific view only a user can see (like how many shares)
from .services import fetch_pokemon_data
import requests
from requests_oauthlib import OAuth1
from backend.settings import env
# Create your views here.

#view all pokemon
class All_pokemon(APIView):
    def get(self, request):
        all_pkmn = PkmnStock.objects.all()
        serializer = PkmnStockSerializer(all_pkmn, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

#view pokemon info REQUIRES LOGIN
class Pokemon_info(APIView):
    def get(self, request, pokemon_id):
        if isinstance(pokemon_id, int):  # Check if the input is an integer
            try:
                pokemon = PkmnStock.objects.get(pokedex_id=pokemon_id)  # Fetch from local DB
            except PkmnStock.DoesNotExist:
                pokemon = None
        else:  # The input is a string
            try:
                pokemon = PkmnStock.objects.get(name=pokemon_id.title())
            except PkmnStock.DoesNotExist:
                pokemon = None

        # if Pokémon is not in local DB, fetch from PokeAPI
        if not pokemon:
            data = fetch_pokemon_data(pokemon_id)  # fetch data from PokeAPI
            if not isinstance(data, dict):
                return Response({'error': 'No data available from PokeAPI or it is a legendary / mythical Pokémon.'}, status=HTTP_404_NOT_FOUND)
            
            # create Pokémon in local DB
            pokemon = PkmnStock.objects.create(
                name=data.get('name').title(),
                pokedex_id=data.get('pokedex_id'),
                description=data.get('description'),
                what_type=data.get('types'),
                base_stats=data.get('base_stats'),
                move_count=data.get('move_count'),
                moves=data.get('moves'),
                base_price=data.get('base_price'),
                evolution_stages=data.get('evolution_stages')
            )

        # fetch type icons from the Noun Project
        icons = {}
        for poke_type in pokemon.what_type:
            icons[poke_type] = self.get_icon_url(poke_type)

        # serialize the Pokémon data
        serializer = PkmnStockSerializer(pokemon)
        serialized_data = serializer.data
        serialized_data['icons'] = icons  # add icons to the response

        print(f"Name: {pokemon.name} || Pokedex ID: {pokemon.pokedex_id} || Price: {pokemon.base_price}")
        return Response(serialized_data, status=HTTP_200_OK)

    def get_icon_url(self, name):
        auth = OAuth1(env.get("NOUN_API_KEY"), env.get("NOUN_API_SECRET"))
        endpoint = f"https://api.thenounproject.com/v2/icon/?query={name}&limit=1"

        response = requests.get(endpoint, auth=auth)
        response_data = response.json()

        if "icons" in response_data and len(response_data["icons"]) > 0:
            thumbnail_url = response_data["icons"][0]["thumbnail_url"]
            return thumbnail_url
        return None