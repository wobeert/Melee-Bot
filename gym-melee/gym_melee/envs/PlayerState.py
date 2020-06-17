# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:55:29 2020

@author: wobee
"""
from enum import Enum
import Controller
from KeyBoard import KeyBoard

class PlayerType(Enum):
    HUMAN= 0
    AI = 1
        
class PlayerState():
    def __init__(self, percent=0, stocks=4, character='Unknown'):
        self.percent = percent
        self.stocks = stocks
        self.character = character


        