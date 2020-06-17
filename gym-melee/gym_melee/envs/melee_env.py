# -*- coding: utf-8 -*-
"""
Created on Sat May  2 17:20:58 2020

@author: wobee
"""


import gym
from gym import error, spaces, utils
from .GameState import GameStateManager, PlayerState
from .Contrllers.KeyBoard import KeyBoard
import numpy as np
FRAME_WIDTH = 640
FRAME_HEIGHT = 524
STOCK_OFFSET = 10 # TODO: Need to calculate how far apart each stock is

# button_space = spaces.Discrete(len(Button))
# analog_stick_space = spaces.Box(len(Stick))
# c_stick_space = spaces.Box(len(Stick))
# controller_space = spaces.Tuple((button_space, analog_stick_space, c_stick_space))

class MeleeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, frame_path, ai_port, opponent_port):
        
        self.game_state = GameStateManager(frame_path)
        self.ai_controller = KeyBoard()
        
        self.prev_ai_state = PlayerState()
        self.prev_opponent_state = PlayerState()
        
        self.observation_space = spaces.Box(low=0, high=255, shape=(FRAME_WIDTH, FRAME_HEIGHT, 3), dtype=np.uint8)
        self.action_space = self.ai_player.controller.get_action_space()
        

    def step(self, action):
        self._take_action(action) 
        self.update_game_state()
        reward = self._get_reward()
        
        return self.game_state.frame, reward, self.game_state.game_over, {}
    
    def update_game_state(self):
        # Save current player states as previous states
        self.prev_ai_state.update(self.game_state.ai_state)
        self.prev_opponent_state.update(self.game_state.opponent_state)
        self.game_state.update()
        return
        

    def reset(self, reset_match=False):
        if reset_match:
            self.ai_player_controller.reset_game()
        else:
            self.game_state.start()
            # TODO: implement resetting frame_loader
        return self.game_state.frame
        
    def render(self, mode='human'):
        ''' Sets up thee frame loader
        TODO: Start running dolphin from here.
        '''
        pass

    def close(self):
        pass
    
    def _take_action(self, action):
        ''' Sends controller inputs to the game and updates controller state '''
        self.ai_player_controller.send_inputs(action)
        return
        
    def _get_reward(self):
        reward = 0
        
        # Reward for taking stock
        if self.prev_opponent_state.stocks < self.opponent_player.state.stocks:
            reward += 3
        
        # Reward for losing a stock
        if self.prev_ai_state.stocks < self.ai_player.state.stocks:
            reward -= 3
        
        # Reward for hitting opponent
        if self.prev_opponent_state.percent < self.opponent_player.state.percent:
            reward += 1
            
        # Reward for getting hit
        if self.prev_ai_state.percent < self.ai_player.state.percent:
            reward -= 1
        
        # Reward for having more/less/same stocks
        if self.ai_player.state.stocks > self.opponent_player.state.stocks:
            reward += 1
        elif self.ai_player.state.stocks < self.opponent_player.state.stocks:
            reward -= 1
            
        if self.ai_player.state.percent < self.opponent_player.state.percent:
            reward += 2
        elif self.ai_player.state.percent > self.opponent_player.state.percent:
            reward -= 2
        
        return reward
        
        
