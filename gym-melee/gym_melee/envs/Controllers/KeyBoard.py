# -*- coding: utf-8 -*-
"""
Created on Sat May  2 23:01:11 2020

@author: wobee
"""

import ctypes
from gym import spaces
from enum import IntEnum
class Button(IntEnum):
    A = 0
    B = 1
    X = 2
    Z = 3
    L = 4
    UP = 5
    DOWN = 6
    LEFT = 7
    RIGHT =8 
    C_UP = 9
    C_DOWN = 10
    C_LEFT = 11
    C_RIGHT = 12

KEYBOARD_MAPPING = {
    Button.A: 0x1E,               # a key on keyboard
    Button.B: 0x30,               # b key on keyboard
    Button.X: 0x2D,               # x key on keyboard
    Button.Z: 0x2C,               # z key on keyboard
    Button.L: 0x26,               # l key on keyboard
    Button.UP: 0xC8,    # up
    Button.DOWN: 0xD0,  # down
    Button.LEFT: 0xCB,  # left
    Button.RIGHT: 0xCD, # right
    Button.C_UP: 0x14,    # t
    Button.C_LEFT: 0x21,  # f
    Button.C_RIGHT: 0x23, # h
    Button.C_DOWN: 0x22   # g
}

# Keyboard event hexcode
KEYEVENTF_SCANCODE = 0x0008 # Code for detecting when key is pressed
KEYEVENTF_KEYUP = 0x0002

# Function to simulate keyboard/mouse inputs
SendInput = ctypes.windll.user32.SendInput

# C structures used with SendInput
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

def press_key(key):
    assert key in KEYBOARD_MAPPING
    hexKeyCode = KEYBOARD_MAPPING[key]
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, KEYEVENTF_SCANCODE, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release_key(key):
    assert key in KEYBOARD_MAPPING
    hexKeyCode = KEYBOARD_MAPPING[key]
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, KEYEVENTF_SCANCODE | KEYEVENTF_KEYUP, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

BUTTONS = (Button.A, Button.B, Button.X, Button.Z, Button.L, Button.UP, Button.DOWN, Button.LEFT, Button.RIGHT, Button.C_UP, Button.C_DOWN, Button.C_LEFT, Button.C_RIGHT)
from time import sleep
class KeyBoard():
    def __init__(self):
        self.state = [False for _ in range(len(BUTTONS))]

    def press_button(self, button):
        press_key(button)
        self.state[button] = True


    def release_button(self, button):
        release_key(button)
        self.state[button] = False

    def get_action_space(self):
        n_spaces = len(BUTTONS)
        return spaces.MultiBinary(n_spaces)
    
    def send_inputs(self, actions):
        for i, action in enumerate(actions):
            self.process_action(i,action)
            # print(self.state[i], bool(action))
            # if self.process_action(i,action):
            #     print('\tUpdated', self.state[i])
            # print()
            
        
    def process_action(self, button_index, action):
        if self.state[button_index] == bool(action):
            return False
        else:
            # sleep(.05)
            # print(BUTTONS[button_index])
            if bool(action):
                self.press_button(BUTTONS[button_index])
            else:
                self.release_button(BUTTONS[button_index])
            return True
