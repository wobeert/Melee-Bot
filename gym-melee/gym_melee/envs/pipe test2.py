# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:52:08 2020

@author: wobee
"""

import win32pipe, win32file, win32api

# Server
pipe = win32pipe.CreateNamedPipe(
        r"\\.\Pipe\Bot1",
        win32pipe.PIPE_ACCESS_DUPLEX,
        win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT,
        1, 65536, 65536,
        0,
        None)
connect = win32pipe.ConnectNamedPipe(pipe, None)


# Client
handle = win32file.CreateFile(
        r'\\.\Pipe\0\Bot1',
        win32file.GENERIC_READ | win32file.GENERIC_WRITE,
        0,
        None,
        win32file.OPEN_EXISTING,
        0,
        None)
res = win32pipe.SetNamedPipeHandleState(handle, win32pipe.PIPE_READMODE_MESSAGE, None, None)
res = win32file.ReadFile(handle, 64*1024)


win32file.WriteFile(pipe, str.encode(f'this is a test'))