# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 19:44:29 2025

@author: User
"""

#TODO pick election winners
#TODO add plot / histogram of who wins
#TODO add voters willingness to participate
#TODO add voters set_favorite_party
#TODO have other parties adapt their ideologies ?
#TODO add political campaigns


from simulation_environment import Simulation


            
        
        
Sim = Simulation()

Sim.generate_party_list(5)
Sim.generate_voter_list(500)
Sim.election_day()







