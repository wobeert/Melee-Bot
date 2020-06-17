# -*- coding: utf-8 -*-
"""
Created on Wed May  6 04:08:03 2020

@author: wobee
"""

import subprocess

def get_reader_writer():
    fd_read, fd_write = os.pipe()
    return [os.fdopen(fd_read, 'r'), os.fdopen(fd_write, 'w')]


cmd = ['Dolphin.exe'] 
p1 = os.popen(cmd,mode='w')
# process = subprocess.Popen(cmd, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
 

# Creates pipe
pipe = win32pipe.CreateNamedPipe(
        r"\\.\Pipe\Bot1",
        win32pipe.PIPE_ACCESS_DUPLEX,
        win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT,
        1, 65536, 65536,
        0,
        None)