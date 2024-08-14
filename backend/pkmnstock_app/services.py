#this will call the pokeAPI
#this will be called the service layer, it 'serves' the purpose of calling apis
#helps with the 'single responsibility' design

import requests

def fetch_pokemon_data(name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
    if response.status_code == 200:
        return response.json()
    else:
        return None