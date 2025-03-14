# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 21:22:48 2025

@author: User
"""

class PoliticalParticipant:
    def __init__(self):
        self.name : str = None
        self.ideology : int = None
        
    def setName(self, name : str):
        if (type(name) == str):
            self.name = name
        else :
            print("type error")
        
    def setIdeology(self, ideology : int):
        
        if (type(ideology) == int):
            
            if 0 < ideology < 100: 
                self.ideology = ideology
                
            else :
                print("value error")
                
        else :
            print("type error")