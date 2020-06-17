# -*- coding: utf-8 -*-
"""
Created on Mon May  4 10:46:38 2020

@author: wobee
"""

import cv2 as cv
class FrameLoader():
    ''' Reads frames from dump created by dolphin.
    
    '''
    def __init__(self, path, frame_size=(640, 524), color_scale=cv.COLOR_BGR2RGB):
        # TODO: Change constant frame size in channel index
        self.frame_size = (*frame_size, 3)
        self.color_scale = color_scale
        self.video_capture = cv.VideoCapture(path)
        self.frame_index = 0
        assert self.video_capture.isOpened(), f"Error opening {path}"
    
    def next_frame(self, skip_nframes=0):
        # Skip frames
        for _ in range(skip_nframes):
            self.video_capture.grab()
            self.frame_index += 1
        status, frame = self.video_capture.read()
        self.frame_index += 1
        assert status, "Failed to get frame"
        frame = self.process_frame(frame)
        return status, frame
    
    def get_frame_index(self):
        return self.frame_index
        
    
    def last_frame(self):
        while self.video_capture.grab(): 
            self.frame_index += 1
        self.video_capture.set(cv.CAP_PROP_POS_FRAMES, self.frame_index-1)
        return self.next_frame()
    
    def process_frame(self, frame):
        frame = cv.resize(frame, (self.frame_size[0], self.frame_size[1]))
        if self.color_scale is not None:
            frame = cv.cvtColor(frame, self.color_scale)
        return frame
    