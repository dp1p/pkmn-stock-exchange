from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from requests_oauthlib import OAuth1
from backend.settings import env
# Create your views here.
class Noun_Project(APIView):
    def get(self, request, name):
        auth = OAuth1(env.get("NOUN_API_KEY"), env.get("NOUN_API_SECRET"))
        endpoint = f"https://api.thenounproject.com/v2/icon/?query={name}&limit=1"

        response = requests.get(endpoint, auth=auth)
        response_data = response.json()
        
        thumbnail_url = response_data["icons"][0]["thumbnail_url"]
        print(thumbnail_url)
        return Response(thumbnail_url)

