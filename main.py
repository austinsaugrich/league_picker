from champion import Champion
import json
import sys
import random
# champ = Champion()
# print(champ.name)

champions = []



def random_champ():
    champ_count = len(champions)
    return random.randint(1, champ_count) - 1
    

def load_champ():
    with open('./leaguelist.json') as champs_file:
        data = json.load(champs_file)
        for champs in data:
             champions.append(champs)

    
load_champ()
id = random_champ()
print(champions[id])