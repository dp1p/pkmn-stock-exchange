from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from .models import Watchlist
from .serializers import WatchlistSerializer #to see json information from the model
from user_app.views import TokenReq #this is user specific, this user can access THEIR watchlist

#CRUD MODEL 

# CREATE a watchlist
class CreateWatchlist(TokenReq):
    def post(self, request):
        new_watchlist = WatchlistSerializer(data=request.data) #we create a new watchlist by using the Watchlist serializer
        new_watchlist.save()
        return Response(new_watchlist, status=HTTP_201_CREATED)

# #READ your watchlist
# class GetWatchlist(TokenReq):
#     def get(self, request):
#         #get a list of all the pkmn which our watchlist has
#         pokemon = instance.pokemon.all()
#         #turns the list of obj to list of dictionaries
#         ser_pokemon = [{'name': p.name} for p in pokemon]
#         return ser_pokemon
