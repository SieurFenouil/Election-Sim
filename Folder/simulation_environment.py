# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 18:48:58 2025

@author: User
"""

import random as rd

from voter import Voter
from party import Party

from party_name_generator import generate_party_name
from voter_name_generator import generate_voter_name

class Simulation():
    def __init__(self):
        self.voterList : list[Voter] = []
        self.partyList : list[Party] = []
        
    def generate_voter_list(self, listSize):

        for i in range(listSize):
            voter = Voter()
            newName = generate_voter_name()
            
            self.voterList.append(voter)
            self.voterList[i].name = newName
            self.voterList[i].ideology = rd.randint(0,100)
            
    def generate_party_list(self, listSize):
                
        for i in range(listSize):
            party = Party()
            newName = generate_party_name()
            
            self.partyList.append(party)
            self.partyList[i].name = newName
            self.partyList[i].ideology = rd.randint(0,100)
        
        self.partyList = sort_parties(self.partyList)
        
        
            
def sort_parties(partyList : list[Party]):    
    return sorted(partyList, key =lambda Party: Party.ideology)
            
    
    