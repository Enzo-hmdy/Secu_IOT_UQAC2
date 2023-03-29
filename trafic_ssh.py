#!/usr/bin/python3
# Description: This script is used to generate a traffic on a ssh server
# Usage: python3 trafic_ssh.py <server_ip> <server_port>
# Example: python3 trafic_ssh.py

import time
import random
import os
import sys
import paramiko

# get the server ip and port from the command line arguments if port is not specified, use the default port 22
ip = sys.argv[1]
port = int(sys.argv[2]) if len(sys.argv) > 2 else 22

# create a new ssh client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connect to the server
client.connect(ip, port=port)

# get the sftp client
sftp = client.open_sftp()



# generate 20 files with random content in the current directory where the script is executed
def generate_files():
    for i in range(20):
        filename = f"file{i}.txt"
        content = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=100))
        with open(filename, "w") as f:
            f.write(content)

# delete all files in the current directory where the script is executed
def delete_files():
    files = os.listdir()
    for file in files:
        os.remove(file)

# list some actions to perform
actions = [
    "touch test.txt",
    "echo 'Hello World!' > test.txt",
    "ls -l",
    "mkdir test cd test touch test.txt echo 'Hello World!' > test.txt",
    "rm -rf test",
    "cd /",
    "cd /home/user",
    "cp myfile.txt /home/user/myfile-copy.txt",
    "mv myfile.txt myrenamedfile.txt",
    "uname -a",
    "df -h",
    "tail /var/log/messages",
    "./myscript.sh",
    "export MY_VAR=myvalue"
]

# main loop
if __name__ == "__main__":
    start_time = time.time() # get the current time
    # delete all files in the current directory where the script is executed
    delete_files()
    # generate 20 files with random content in the current directory where the script is executed
    generate_files()
    # loop for 2 hours
    while time.time() - start_time < 7200:
            # execute the action in a interval of 2 and 7 minutes
            time.sleep(random.randint(120, 420))
            # get a random action
            action = random.choice(actions)
            # execute the action
            stdin, stdout, stderr = client.exec_command(action)
            # print the output
            print(stdout.read().decode())




