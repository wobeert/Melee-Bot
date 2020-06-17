# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:34:43 2020

@author: Robert Lopez
"""

from enum import Enum, IntEnum
# from KeyBoard import press_key, release_key
class ControllerType(Enum):
    GAMECUBE = 0
    STANDARD = 1
    KEYBOARD = 3

class Button(IntEnum):
    A = 0
    B = 1
    X = 2 # Y = 2
    Z = 3
    L = 4 # R = 4
    START = 5
    # D_UP = 6
    # D_DOWN = 7
    # D_LEFT = 8
    # D_RIGHT = 9

class Trigger(Enum):
    L = 0
    # R = 1

class Stick(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class ControllerState:
    def __init__(self, digital_stick):
        self.button = dict([(b,False) for b in Button])

        if digital_stick:
            self.main_stick = {s:False for s in Stick}
            self.c_stick = {s:False for s in Stick}
        else:
            self.main_stick = (.5, .5)
            self.c_stick = (.5, .5)

        self.left_trigger = False
        # self.right_trigger= 0

    def __str__(self):
        string = ""
        for key, val in self.button.items():
            string += f"{str(key).upper()}: {str(val)}"
            string += "\n"
        string += "MAIN_STICK: " + str(self.main_stick) + "\n"
        string += "C_STICK: " + str(self.c_stick) + "\n"
        string += "LEFT_TRIGGER: " + str(self.left_trigger) + "\n"
        # string += "right_trigger: " + str(self.right_trigger) + "\n"
        return string

class Controller:
    ''' Base class for all controller types that keep track of the controllers state.
    Each derived implements its own way of handling the controller
    '''
    def __init__(self, port, digital_stick):
        self.port = port
        self.state = ControllerState(digital_stick)
        self.inputs  = []

    def press_button(self, button):
        assert button in Button, "Unknown button."

    def release_button(self, button):
        assert button in Button, "Unknown button."

    def press_trigger(self, trigger, amount=1):
        assert trigger in Trigger, "Unknown trigger"
        pass

    def move_analog_stick(self, direction, amount=1):
        assert direction in Stick, "Unknown analog stick movement."
        pass

    def move_c_stick(self, direction):
        assert direction in Stick, "Unknown c stick movement."
        pass

    def get_action_space(self):
        pass



# class KeyBoard(Controller):
#     def __init__(self):
#         super().__init__("KeyBoard")

#     def press_button(self, button):
#         super().press_button(button)
#         press_key(button)

#     def release_button(self, button):
#         super().release_button(button)
#         release_key(button)

#     def press_trigger(self, trigger, amount):
#         super().press_trigger(trigger)

#     def release_trigger(self, trigger):
#         super().release_trigger(trigger)
