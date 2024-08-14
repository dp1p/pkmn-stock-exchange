from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from .models import PkmnStock
from .serializers import PkmnStockSerializer #to see json information from the model
from user_app.views import TokenReq #if there is a specific view only a user can see (like how many shares)

# Create your views here.

#view all pokemon
class All_pokemon(APIView):
    def get(self, request):
        all_pkmn = PkmnStock.objects.all()
        serializer = PkmnStockSerializer(all_pkmn, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

#view pokemon info REQUIRES LOGIN
class Pokemon_info(TokenReq): 
    def get(self, request, id):
        try: #see if the id is a number
            type(id) == int
            pokemon = PkmnStock.objects.get(id = id)
        except ValueError:   #if it is not a number 
            try: #see if the id is a str
                pokemon = PkmnStock.objects.get(name=id.title())
            except PkmnStock.DoesNotExist: #if the pokemon name isnt found
                return Response({'error': 'No Pokemon found with provided name'}, status=HTTP_404_NOT_FOUND)
        except PkmnStock.DoesNotExist: #if the pokemon id isnt found
                return Response({'error': 'No Pokemon found with provided ID'}, status=HTTP_404_NOT_FOUND)
        
        serializer = PkmnStockSerializer(pokemon)
        return Response(serializer.data, status=HTTP_200_OK)
                
            
            
        #         if not pokemon: #if pokemon id does not exist in the api
        #              return Response({'error':'No Pokemon or ID found'}, status=HTTP_400_BAD_REQUEST)
        #     elif type(id) == str: 
        #         pokemon = PkmnStock.objects.get(name = id.title())
        #         if not pokemon: #if pokemon name does not exist in the api
        #              return Response({'error':'No Pokemon or ID found'}, status=HTTP_400_BAD_REQUEST)
                
        #     serializer = PkmnStockSerializer(pokemon)
        #     return Response(serializer.data, status=HTTP_200_OK)
        # except ValueError:
        #     return Response({'error':'No Pokemon or ID found'}, status=HTTP_400_BAD_REQUEST)
        
        


        # try: #check if the user enters a number to search AND if primary key is an integer
        #     pk = int(pk_or_name) #convert primary key to an int first
        #     pkmn = PkmnStock.objects.get(pk=pk) #finds the pkmn asscoiated with pk
        # except ValueError: #if it is unable to convert to an integer
        #     pkmn = PkmnStock.objects.filter(pkmn__iexact=pk_or_name) #filters the all the pkmnStock names to find the specfic pkmn
        # except PkmnStock.DoesNotExist: #handles does not exist
        #         return Response({'error': 'Pokemon Name / ID does not exist'}, status=HTTP_400_BAD_REQUEST)
        
        # serializer = PkmnStockSerializer(pkmn)
        # return Response(serializer.data, HTTP_200_OK)
            

