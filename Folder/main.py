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

import copy

from simulation_environment import Simulation


def ElectionDay(voterList, partyList):
        
    for voter in voterList:
        favoriteParty = partyList[0]
        
        for party in partyList:
            if (abs(party.ideology - voter.ideology) < abs(favoriteParty.ideology - voter.ideology)):
                favoriteParty = party
                
        favoriteParty.add_vote()
            
        
        
Sim = Simulation()

Sim.generate_party_list(5)
Sim.generate_voter_list(500)
        

ElectionDay(Sim.voterList, Sim.partyList)







