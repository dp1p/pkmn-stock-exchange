from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from decimal import Decimal
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from .models import Portfolio, PkmnPortfolio
from .serializers import PortfolioSerializer, PkmnPortfolioSerializer #to see json information from the model
from user_app.views import TokenReq #this is user specific, this user can access THEIR watchlist
from pkmnstock_app.views import Pokemon_info #to call this func to add pkmn to a watchlist
from pkmnstock_app.models import PkmnStock #to get the pkmn 

#CRUD MODEL
#CREATE your portfolio
class Create_portfolio(TokenReq):
    def post(self, request):
        if Portfolio.objects.filter(user=request.user).exists():  # check if the user already has a portfolio
            return Response({"message": "You already have a portfolio."}, status=HTTP_400_BAD_REQUEST)
        
        portfolio_data = request.data.copy() #make mutable copy of user data
        portfolio_data['user'] = request.user.id  # grab user's id and add it to the data
        
        serializer = PortfolioSerializer(data=portfolio_data) # pass modified data to the serializer
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

#READING portfolio
class View_portfolio(TokenReq):
    def get(self, request):
        try:
            portfolio = Portfolio.objects.get(user=request.user) #grabs the user's portfolio
            ser_portfolio = PortfolioSerializer(portfolio) #serialize the the user's data
            return Response(ser_portfolio.data, status=HTTP_200_OK) #return it
        except Portfolio.DoesNotExist:
            return Response({"message" : "You have no portfolio yet."}, status=HTTP_204_NO_CONTENT)
    
#UPDATING PORTFOLIO
class Buy_portfolio(TokenReq):
    def post(self, request):
        pokemon_id_or_name = request.data.get('pokemon_id_or_name')  #grab the users request of the pkmn they want to buy
        shares_purchased = int(request.data.get('shares_purchased', 1)) #how many shares the user wants to buy

        if pokemon_id_or_name.isdigit(): # if the user enters a pokedex no. / and is in our local db in 'pkmnstock' model
            try:
                pokemon = PkmnStock.objects.get(pokedex_id=int(pokemon_id_or_name)) 
            except PkmnStock.DoesNotExist:
                response = Pokemon_info().get(request, pokemon_id_or_name) # if not found in local db, fetch from PokeAPI and create it, which pkmn_info utlizies and creates the instance automatically
                if response.status_code == HTTP_200_OK:
                    pokemon = PkmnStock.objects.get(pokedex_id=int(pokemon_id_or_name)) #grab that pokedex number
                else:
                    return Response({'error': 'No data available from PokeAPI or it is a legendary / mythical Pokémon.'}, status=HTTP_404_NOT_FOUND)
        else: #if the user enters a str name
            try:
                pokemon = PkmnStock.objects.get(name=pokemon_id_or_name.title())
            except PkmnStock.DoesNotExist:
                response = Pokemon_info().get(request, pokemon_id_or_name)
                if response.status_code == HTTP_200_OK:
                    pokemon = PkmnStock.objects.get(name=pokemon_id_or_name.title())
                else:
                    return Response({'error': 'No data available from PokeAPI or it is a legendary / mythical Pokémon.'}, status=HTTP_404_NOT_FOUND)

       
        portfolio = Portfolio.objects.get(user=request.user)  # grab the user's portfolio

        
        base_price = Decimal(pokemon.base_price)    #convert the jsonfield from 'pkmnstock' model to be a decimal 
        total_purchase_cost = base_price * shares_purchased #find the total purchase cost

        
        if portfolio.buying_power < total_purchase_cost: # make sure the user has enough buying power
            return Response({"error": "Not enough buying power to complete the purchase.", "name" : f"{pokemon.name}", "price" : f"{base_price}", "buying_power": f"{portfolio.buying_power}"},
                            status=HTTP_400_BAD_REQUEST
                            )

        
        pkmn_portfolio, created = PkmnPortfolio.objects.get_or_create( # get or create the portfolio entry for the pkmnstock being added
            portfolio=portfolio, pokemon=pokemon,
            defaults={'shares_purchased': shares_purchased, 'total_price': total_purchase_cost}  #if the Pokémon is not already in the portfolio, create a new entry with the given shares and total price using the serializer
        )

        if not created: #if that pkmn entry in our portfolio has already existed, just update
            pkmn_portfolio.shares_purchased += shares_purchased
            pkmn_portfolio.total_price += total_purchase_cost
            pkmn_portfolio.save()

        
        portfolio.buying_power -= total_purchase_cost # SUBTRACT the purchase cost of a pkmn from the user's buying power)
        portfolio.total_portfolio += total_purchase_cost #ADD the purchase cost to our pkmn stock portfolio
        portfolio.save()

        ser_portfolio = PortfolioSerializer(portfolio)
        return Response(ser_portfolio.data, status=HTTP_200_OK)