# -*- coding: utf-8 -*-
"""
Created on Tue May  5 14:26:02 2020

@author: wobee
"""

import cv2 as cv
def show_image(img):
    cv.imshow('image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return