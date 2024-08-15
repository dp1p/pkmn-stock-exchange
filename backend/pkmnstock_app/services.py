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

        # for values in base_stats.keys():
        #     print(values)
        # for keys in base_stats.keys():
        #     print(keys)

        base_price = 0
        #to figure out the price:
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


            # print(stat_name, base_stats[stat_name]) #print the stat name, stat value 
            # base_price += base_stats[_]
            # case

        print(f"base price total: {base_price}")


        


        return {
            # 'name': data['name'].title(),
            # 'pokede__id': data['id'],
            # 'base_stats': base_stats,
            # 'types': types,
            # 'move_count': len(moves),
            # 'moves': moves

        }

    
    else:
        return None

#this is for testing and running just services.py
pokemon = fetch_pokemon_data('charizard')
print(pokemon)