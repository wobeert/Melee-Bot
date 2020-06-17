# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:54:51 2020

@author: wobee
"""
from .FrameLoader import FrameLoader

# Pixel locations of player stock/percent with normal icons
STOCK_Y = [200,210]
PERCENT_Y = [222,242]
PLAYER_X_OFFSET = 74
STOCK_X_OFFSET = 14
P1_X= [11,67] # 56
P2_X = [P1_X[0]+PLAYER_X_OFFSET,P1_X[1]+PLAYER_X_OFFSET]

# TODO: Pixel locations of player stock/percent with pal icons

class PlayerState():
    def __init__(self, percent=0, stocks=4, character='Unknown'):
        self.percent = percent
        self.stocks = stocks
        self.character = character
    
    def update(self, new_state):
        self.percent = new_state.percent
        self.stocks = new_state.stocks
        self.character = new_state.character

class GameStateManager():
    def __init__(self, frame_path):
        self.frame_loader = FrameLoader(frame_path)
        self.frame = None
        self.game_over = False
        self.opponent = PlayerState()
        self.ai = PlayerState()
        return
    
    def start(self):
        self.frame = self.frame_loader.last_frame()
        self.ai_stock_icon = self.frame[STOCK_Y[0]:STOCK_Y[1],
                                  P1_X[1]-STOCK_X_OFFSET:P1_X[1],:]
        
        self.opponent_stock_icon = self.frame[STOCK_Y[0]:STOCK_Y[1],
                                  P2_X[1]-STOCK_X_OFFSET:P2_X[1],:]

        
    def update(self):
        _, self.frame = self.frame_loader.next_frame()
        
        self._update_player_states()
        
        if self.ai.stocks == 0 or self.opponent.stocks == 0:
            self.game_over = True
        else:
            self.game_over = False
        return
    
    def _update_player_states(self):
        # update stock count
        self._update_stocks()
        self._update_percents()
        
    def _count_stocks(self):
        pass
    
    def _count_percents(self):    
        pass
        