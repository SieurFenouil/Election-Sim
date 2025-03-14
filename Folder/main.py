# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 19:44:29 2025

@author: User
"""

#TODO add plot / histogram of who wins
#TODO add voters willingness to participate
#TODO add voters set_favorite_party
#TODO have other parties adapt their ideologies ?
#TODO add political campaigns


from simulation_environment import Simulation

def launch_simulation():
    
    elections_number = int(input( "how many elections ?"))
    parties_number = int(input( "how many parties ?"))
    voters_number = int(input( "how many voters ?"))
            
    Sim = Simulation()
    
    Sim.generate_party_list(parties_number)
    
    for i in range(elections_number):
    
        print( "----- Year ", i+1, " -----")
        Sim.generate_voter_list(voters_number)
        Sim.election_day()







