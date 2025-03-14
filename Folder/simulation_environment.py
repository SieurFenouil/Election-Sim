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

        self.voterList = []
        
        for i in range(listSize):
            voter = Voter()
            newName = generate_voter_name()
            
            self.voterList.append(voter)
            self.voterList[i].name = newName
            self.voterList[i].ideology = rd.randint(0,100)
            
    def generate_party_list(self, listSize):
        
        self.partyList = []
                
        for i in range(listSize):
            party = Party()
            newName = generate_party_name()
            
            self.partyList.append(party)
            self.partyList[i].name = newName
            self.partyList[i].ideology = rd.randint(0,100)
        
    
    def election_day(self):
            
        for voter in self.voterList:
            favoriteParty = self.partyList[0]
            
            for party in self.partyList:
                if (abs(party.ideology - voter.ideology) < abs(favoriteParty.ideology - voter.ideology)):
                    favoriteParty = party
                    
            favoriteParty.add_vote()
                
        self.partyList = sort_parties_by_votes(self.partyList)
        
        for party in self.partyList:
            print(party.name, "have gotten", party.votes, "votes, and believe in", party.ideology)
            party.votes = 0
            
        
        
        
            
def sort_parties_by_ideology(partyList : list[Party]):    
    return sorted(partyList, key =lambda Party: Party.ideology)
            
def sort_parties_by_votes(partyList : list[Party]):    
    return sorted(partyList, key =lambda Party: Party.votes)
            
    
    