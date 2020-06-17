# -*- coding: utf-8 -*-
"""
Created on Sun May 17 10:45:23 2020

@author: wobee
"""



''' notes on how to get the melee bot to learn

# Related concepts
image reconstruction
meta learning, (MLSH)

# Step into the environment (take action).
state = env.step(action)

reward, val, action = get_reward_value_action(state)

# this function takes in curent state and action taken at that state in order
# to predict the next state
pred_next_state = predict_state(state, action)

reward, val, action = get_reward_value_action(pred_next_state)

# backprop with the correct values



'''
def get_reward(state):
    pass
def get_reward_value_action(state):
    reward = get_reward(state)
    value = value_function(state, prev_state, prev_action)
    action = policy(state)
    pass

# returns predicted future state
def predict_state(state):
    pass

# returns action to take
def policy(state):
    pass

# Returns the value of a current state, given the prev action taken in the prev state.
def value_function(state, prev_state, prev_action):
    pass