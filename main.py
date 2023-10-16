from champion import Champion
import json
import sys
import random
# champ = Champion()
# print(champ.name)

champions = []
lane_choice = "Jungle"
attack_type = "Ranged"
damage_type = "AP"


def get_lane(lanes):
    if lane_choice in lanes:
        return True
    return False

def get_attack(at):
    if attack_type in at:
        return True
    return False

def get_damage_type(dt):
    if damage_type in dt:
        return True
    return False

def random_champ():
    champ_count = len(champions)
    return random.randint(1, champ_count) - 1
    
def load_champ():
    with open('./leaguelist.json') as champs_file:
        data = json.load(champs_file)
        for champs in data:
             if get_lane(champs["lane"]):
                if get_attack(champs["attack"]):
                    if get_damage_type(champs["damagetype"]):
                        champions.append(champs)

    
load_champ()
id = random_champ()
print(champions)