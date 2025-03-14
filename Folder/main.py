# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 19:44:29 2025

@author: User
"""

#TODO add plot / histogram of who wins

#TODO do ideology as multidimentional tuple

#TODO parties
# - add popularity attribute
# - change popularity based on number of votes and donations
# - extra random popularity hit for election winners. ( scales with ideology ?)
# - ideological changes to match voter average
# - ideological changes to match base average
# - willingness to change ideology ( scales with ideology ?)

#TODO voters
# - willingness to participate. ( scales with ideology ?)
# - willingness to donate. ( scales with ideology ?)
# - voters get closer to one another
# - voters get attracted to parties (see gravity and planets)
# - random big drifts every few elections
# - willingness to change ideology ( scales with ideology ?)



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







