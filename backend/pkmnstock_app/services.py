#this will call the pokeAPI
#this will be called the service layer, it 'serves' the purpose of calling apis
#helps with the 'single responsibility' design

import requests

def fetch_pokemon_data(pokemon_id):
    if isinstance(pokemon_id, int):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    else:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id.lower()}/"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None