from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from .models import Watchlist
from .serializers import WatchlistSerializer #to see json information from the model
from user_app.views import TokenReq #this is user specific, this user can access THEIR watchlist
from pkmnstock_app.views import Pokemon_info #to call this func to add pkmn to a watchlist
from pkmnstock_app.models import PkmnStock #to get the pkmn 

#CRUD MODEL 

# CREATE a watchlist
class Create_watchlist(TokenReq):
    def post(self, request):
        watchlist_name = request.data.get('name')

        if Watchlist.objects.filter(name=watchlist_name).exists(): #if watchlist already exists
            return Response({'message': f" '{watchlist_name}' already exists."}, status=HTTP_400_BAD_REQUEST)
        
        watchlist_data = request.data.copy()

        new_watchlist = WatchlistSerializer(data=watchlist_data, context={'request': request}) #we create a new watchlist by using the Watchlist serializer, but use the context of the user
        if new_watchlist.is_valid(): #checks that it passes the model parameters 
            new_watchlist.save()
            return Response(new_watchlist.data, status=HTTP_201_CREATED)
        else:
            return Response(new_watchlist.errors, status=HTTP_400_BAD_REQUEST)
            
# READ ALL watchlist
class All_watchlist(TokenReq):
    def get(self, request):
        #grabs ALL the users watchlist
        all_watchlists = Watchlist.objects.all()
        if all_watchlists.exists():
            ser_watchlists = WatchlistSerializer(all_watchlists, many=True)
            return Response(ser_watchlists.data, status=HTTP_200_OK)

        return Response({"message" : "You have no watchlists"}, status=HTTP_204_NO_CONTENT)
        

#READ a specfic watchlist
class Get_watchlist(TokenReq):
    def get(self, request, watchlist_name):
        #grabs SPECIFIC the users watchlist
        try:
            watchlist_name = Watchlist.objects.get(name=watchlist_name)
        except Watchlist.DoesNotExist: #if that watchlist name does not exist
            return Response({"message" : f"You do not have the watchlist '{watchlist_name}' "}, status=HTTP_404_NOT_FOUND)
        
        ser_watchlist = WatchlistSerializer(watchlist_name)
        return Response(ser_watchlist.data, status=HTTP_200_OK)

#UPDATE a watchlist 
class Update_watchlist(TokenReq):
    def put(self, request, watchlist_name):
        try:
            watchlist = Watchlist.objects.get(name=watchlist_name)
        except Watchlist.DoesNotExist:
            return Response({'message' : f"'{watchlist_name}' does not exist."}, status=HTTP_404_NOT_FOUND)
        
        #grab the pokedex_id the user request either name or by id thanks to pokmeon info handling str and ints
        pokemon_id_or_name = request.data.get('pokemon_id_or_name')
        if not pokemon_id_or_name:
            return Response({"message": "Please provide a Pokémon name or Pokédex ID."}, status=HTTP_400_BAD_REQUEST)
        
       # fetch the pokemon by ID or name
        if pokemon_id_or_name.isdigit():
            pokemon = get_object_or_404(PkmnStock, pokedex_id=pokemon_id_or_name)
        else:
            pokemon = get_object_or_404(PkmnStock, name=pokemon_id_or_name.title())
        
        watchlist.pokemon.add(pokemon) #call the 'pkmnstock' model through 'pokemon', so we can grab the obj from the model and add it to 'watchlist'
        # save updated watchlist
        watchlist.save()

        # serialize and return the updated watchlist
        ser_watchlist = WatchlistSerializer(watchlist)
        return Response(ser_watchlist.data, status=HTTP_200_OK)

#DELETE a pokemon from watchlist
class Delete_from_watchlist(TokenReq):
    def delete(self, request, watchlist_name):
        try:
            watchlist = Watchlist.objects.get(name=watchlist_name)
        except Watchlist.DoesNotExist:
            return Response({'message' : f"'{watchlist_name}' does not exist."}, status=HTTP_404_NOT_FOUND)
        
        #grab the pokedex_id the user request either name or by id thanks to pokmeon info handling str and ints
        pokemon_id_or_name = request.data.get('pokemon_id_or_name')
        if not pokemon_id_or_name:
            return Response({"message": "Please provide a Pokémon name or Pokédex ID."}, status=HTTP_400_BAD_REQUEST)
        
       # fetch the pokemon by ID or name
        if pokemon_id_or_name.isdigit():
            pokemon = get_object_or_404(PkmnStock, pokedex_id=pokemon_id_or_name)
        else:
            pokemon = get_object_or_404(PkmnStock, name=pokemon_id_or_name.title())

        watchlist.pokemon.remove(pokemon)
        watchlist.save()
        # serialize and return the updated watchlist
        ser_watchlist = WatchlistSerializer(watchlist)
        return Response(ser_watchlist.data, status=HTTP_200_OK)


#DELETE entire watchlist
class Delete_watchlist(TokenReq):
    def delete(self, request, watchlist_name):
        try:    #retrieve watchlist by name and the current user
            watchlist = Watchlist.objects.get(name=watchlist_name, user=request.user)
        except Watchlist.DoesNotExist:
            return Response({"message" : f"'{watchlist_name}' does not exist."})
        
        watchlist.delete()
        return Response({'message' : f" '{watchlist_name}' has been deleted."})

