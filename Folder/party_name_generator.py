# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 18:56:35 2025

@author: User
"""

import random as rd

adj_list = ["Long", "Tall", "Thirsty", "Angry", "Cool", "Strange", "Self-aware", "Crouching", "Armed", "Unhinged", "Award-winning",
            "Texan", "Hot", "Conspiring", "Electronic", "Vengeful", "Dyselixc", "Hydro", "Strawberry-flavored"]

animal_list = [" Leopards", " Giraffes", " Salmons", " Elks", " Beavers", " Turtles", " Gators", " Dragonflies", " Goats", " Arthropods",
               " Tigers", " Whales", " Worms", " Puppies", " Eagles", " Ostriches"]

suffix_list = [" 2 : Electric Boogaloo", " for Freedom", " but Better", ", Hidden Dragons", " with Guns", " ++", " from Space",
               " ™©®"]

def generate_party_name():
    
    fullName = ""
    
    random_adj_index = rd.randint(0, len(adj_list) - 1)
    random_animal_index = rd.randint(0, len(animal_list) - 1)
    random_suffix_index = rd.randint(0, len(suffix_list) - 1)
    
    fullName = adj_list[random_adj_index] + animal_list[random_animal_index]
    
    if (rd.randint(0,2) == 2):
        fullName += suffix_list[random_suffix_index]
    
    return fullName
    
        