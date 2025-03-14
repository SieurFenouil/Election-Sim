# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 20:34:50 2025

@author: User
"""

import random as rd

name_list = ["Max", "Johnny", "Leslie", "Alex", "Barbara", "Jean", "Sandra", "Clara", "Ahmed", "Frank", "Fabien",
            "Thomas", "Emilia", "Farah", "Jonah", "Mercy", "Bryan", "Jennifer", "Carlos", "Jocelyn", "Mercedes",
            "Alejandro", "Cecilia", "Julie", "Francesca", "Fabio", "Ricardo", "Philippe", "Charlotte", "Marin",
            "Eric", "Joseph", "Romain", "Michel"]


def generate_voter_name():
    
    random_name_index = rd.randint(0, len(name_list) - 1)
    
    return name_list[random_name_index]