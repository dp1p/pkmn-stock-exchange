from django.shortcuts import render
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import App_user
from portfolio_app.models import Portfolio
from rest_framework.authtoken.models import Token
from rest_framework.status import (
	HTTP_200_OK,
	HTTP_204_NO_CONTENT,
	HTTP_201_CREATED,
	HTTP_400_BAD_REQUEST
)
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class Sign_up(APIView): 
    def post(self, request):# check the user info to see if it is validated, if so, save
        data = request.data.copy()
        data['username'] = data.get('email')  # data['username'] needs to find what our username is set, in this case, it is email
        try: 
            new_user = App_user(**data) 
            new_user.full_clean()
            new_user.set_password(data.get("password"))
            new_user.save() 
            Portfolio.objects.create(user=new_user) # create a portfolio for the new user

            token = Token.objects.create(user=new_user)
            login(request, new_user)  # Log the new user in
            response_data = {'user': new_user.email, 'token': token.key}
            return Response(response_data, status=HTTP_201_CREATED)
        except ValidationError as e:
            raise Response(e.message_dict, status=HTTP_400_BAD_REQUEST)

class Log_in(APIView):
    def post(self, request):
        data = request.data.copy() #requesting what the user inputted
        data['username'] = data.get('email') #data['username'] needs to find what our username is set, in this is email
        user = authenticate(username = data.get('username'), password = data.get("password")) #we make sure username matches the password

        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            response_data = ({'user': user.email, 'token': token.key})
            return Response(response_data, status=HTTP_200_OK)
        
        return ("Username incorrect / does not exist")
    
class TokenReq(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class Log_out(TokenReq):
    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        response_data = "LOGGED OUT SUCCESSFULLY"
        return Response(response_data, status=HTTP_204_NO_CONTENT)
    
class Info(TokenReq):
    def get(self, request):
        return Response({'email': request.user.email})