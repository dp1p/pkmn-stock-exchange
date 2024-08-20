from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from .models import Portfolio
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
    
#UPDATING PORTFOLIO
