# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 21:27:30 2025

@author: User
"""

from  political_participants import PoliticalParticipant


class Party(PoliticalParticipant):
    def __init__(self):
        super().__init__()
        self.votes : int = 0
        self.finalRank : int = 0
       
    def add_vote(self):
        self.votes += 1
        
    def set_final_rank(self, rank):
        self.rank = rank