#this will call the pokeAPI
#this will be called the service layer, it 'serves' the purpose of calling apis
#helps with the 'single responsibility' design
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
import requests, random


#### THE POKEMON PRICE WILL BE DETERMINED BY...
# hp | atk | def | sp atk | sp. def | speed | move count, types, and their evolution stages


#-------function to figure out if pkmn has an evolution stage------------------
def evolution_stage_price(base_price, check_status, pokemon_id):
    evolution_stages = check_status['evolution_chain']['url'] #first grab the url
    evolution_stages = requests.get(evolution_stages).json()  #then grab the json data
    current_stage = evolution_stages['chain'] #Traverse the evolution chain to determine the stage
    stage = 1  # start with the base stage

    pokemon_id = str(pokemon_id).lower()
    
    while current_stage:
        if current_stage['species']['name'] == pokemon_id: #if the current pkmn stage equal to the pkmn name
            break
        if len(current_stage['evolves_to']) == 0:
            break
        elif len(current_stage['evolves_to']) > 0:
            current_stage = current_stage['evolves_to'][0]
            stage += 1  # Increment stage for each evolution
        else:
            current_stage = None

    return ((base_price * stage), stage)  # multiply based on num of stages

#-------function to figure out price------------------
def determine_price(base_stats, moves, types, check_status, pokemon_id):     #grabbing check_status because it has the evolution chain
    base_price = 0
    for stat_name in base_stats: #iterating over dictionary with stat_name
        match stat_name:    #least to greatest when it comes to the influence of the price, starting at 5% ending to 25%
            case 'special-attack':
                _ = base_stats[stat_name] #get the value of the 'stat name'
                base_price += _ + (_*.05) #adding the base stat and increasing it by 5% for price evaulation
            case 'special-defense':
                _ = base_stats[stat_name]
                base_price += _ + (_*.05)
            case 'attack':
                _ = base_stats[stat_name]
                base_price += _ + (_*.10)
            case 'defense':
                _ = base_stats[stat_name]
                base_price += _ + (_*.10)
            case 'hp':
                _ = base_stats[stat_name]
                base_price += _ + (_*.15)
            case 'speed':
                _ = base_stats[stat_name]
                base_price += _ + (_*.20)

    if len(types) == 2: #if the pkmn has two types
        base_price += base_price*.05        #increase by 5%
        
    if len(moves) >= 200:  #if pkmn can learn more than 200 moves (which is mew)
        base_price += base_price*.30
    elif len(moves) >= 150:
        base_price += base_price*.15
    elif len(moves) >= 100:
        base_price += base_price*.10
    elif len(moves) >= 50:
        base_price += base_price*.05
    else:
        base_price += 0


    base_price, stage = evolution_stage_price(base_price, check_status, pokemon_id) #we need to pass in the base_price, our pkmn name we are using, and their status || once passed, we want the return values of BASE PRICE, EVOLUTION STAGE

    



    # print(f'Base Price: {round(base_price,2)}')
    return f"{base_price:.2f}", stage
#--------   MAIN   ----------------------------------------------------------------------------------------------
#function to grab information about pkmn
def fetch_pokemon_data(pokemon_id):
    if isinstance(pokemon_id, int):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
        check_status = f"https://pokeapi.co/api/v2//pokemon-species/{pokemon_id}/" #to get the status if it is a legendary / mythical
    else:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id.lower()}/"
        check_status = f"https://pokeapi.co/api/v2//pokemon-species/{pokemon_id.lower()}/" #to get the status if it is a legendary / mythical

    check_status = requests.get(check_status) #grabs the api information of the pkmn species
    check_status = check_status.json()  #makes it to json
    description = check_status['flavor_text_entries'][0]['flavor_text'] #grabs a the text entry from pokedex
    description = description.replace('\n', ' ')
    description =  description.replace('\f', ' ')

    # print(f'Pokemon: {pokemon_id}')
    # print(description)
    # print(f'Is Legendary? : {check_status['is_legendary']}')
    # print(f'Is Mythical? : {check_status['is_mythical']}')
    if check_status['is_mythical'] == True or check_status['is_legendary'] == True: #checks if the pkmn species is a legendary or mythica;
        return 'pokemonlegendary'
    

    data = requests.get(url) #grabs the api information status

    if data.status_code == 200: #if there is data
        


        data = data.json()
        # to get base stats and their values, and place it in a dict
        base_stats = {}
        for stat in data['stats']:      #to iterate through stats in the data
            stat_name = stat['stat']['name']    #grab the individual stat name
            stat_value = stat['base_stat'] #grab the individual stat value
            base_stats[stat_name] = stat_value  #append it to our dictionary, key is 'stat_name', value is the 'stat_value'

        #to get move names
        moves = [] #will be a list
        for move in data['moves']:
            move_name = move['move']['name']
            moves.append(move_name)

        # get types 
        types = []
        for type_info in data['types']:
            type_name = type_info['type']['name']
            types.append(type_name)
        
        
        base_price, stage = determine_price(base_stats, moves, types, check_status, pokemon_id) #calls a func to determine price based on base_stats, but we also want the evolution stage count so we have to pass by reference?

        return {    #returns all information to the views
            'name': data['name'],
            'pokedex_id': data['id'],
            'description': description,
            'base_stats': base_stats,
            'types': types,
            'move_count': len(moves),
            'moves': moves,
            'base_price': base_price,
            'evolution_stages': stage,
        }
    
    else:
        return None

#this is for testing and running just services.py
# pokemon = fetch_pokemon_data('ditto')