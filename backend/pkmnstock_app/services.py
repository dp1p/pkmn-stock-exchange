#this will call the pokeAPI
#this will be called the service layer, it 'serves' the purpose of calling apis
#helps with the 'single responsibility' design

import requests

def fetch_pokemon_data(pokemon_id):
    if isinstance(pokemon_id, int):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    else:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id.lower()}/"


    data = requests.get(url) #grabs the api information 
    if data.status_code == 200: #if there is data
        data = data.json()
        # Base Stats Loop
        base_stats = {}
        for stat in data['stats']:      #to iterate through stats in the data
            stat_name = stat['stat']['name']    #grab the individual stat name
            stat_value = stat['base_stat'] #grab the individual stat value
            base_stats[stat_name] = stat_value  #append it to our dictionary, key is 'stat_name', value is the 'stat_value'

        #to get move name
        moves = [] #will be a list
        for move in data['moves']:
            move_name = move['move']['name']
            moves.append(move_name)

        # Types Loop
        types = []
        for type_info in data['types']:
            type_name = type_info['type']['name']
            types.append(type_name)


        return {
            'name': data['name'].title(),
            'pokedex_id': data['id'],
            'base_stats': base_stats,
            'types': types,
            'move_count': len(moves),
            'moves': moves

        }

    
    else:
        return None