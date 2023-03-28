#!/bin/python
import ftplib
import time
import random
import os 


# this script simulates a FTP client that connects to a FTP server and downloads or uploads a file
# during 1 hour, betwwen 1 and 5 minutes after each connection, the client will download or upload a file

# the FTP server IP
ip = "172.16.128.130"

# the FTP server port
port = 21

# the FTP server username
username = "ftpuser"

# the FTP server password
password = "azerty"

# the FTP server directory where the files will be uploaded or downloaded
directory = "/home/ftpuser"

# list all files present in the FTP server directory
def list_files():
    ftp = ftplib.FTP() # create a new FTP object
    ftp.connect(ip, port) # connect to the FTP server
    ftp.login(username, password) # login to the FTP server
    ftp.cwd(directory) # change the current working directory to the FTP server directory
    files = ftp.nlst() # list all files in the FTP server directory
    ftp.quit() # quit the FTP session
    return files # return the list of files

def list_file_upload():
    # show the list of files in the current directory where the script is executed and return it as a list
    files = os.listdir()
    return files


# download a file from the FTP server
def download_file(filename):
    ftp = ftplib.FTP() # create a new FTP object
    ftp.connect(ip, port) # connect to the FTP server
    ftp.login(username, password) # login to the FTP server
    ftp.cwd(directory) # change the current working directory to the FTP server directory
    with open(filename, "wb") as f: # open the file in binary write mode
        ftp.retrbinary(f"RETR {filename}", f.write) # download the file from the FTP server
    ftp.quit() # quit the FTP session

# upload a file to the FTP server
def upload_file(filename):
    ftp = ftplib.FTP() # create a new FTP object
    ftp.connect(ip, port) # connect to the FTP server
    ftp.login(username, password) # login to the FTP server
    ftp.cwd(directory) # change the current working directory to the FTP server directory
    with open(filename, "rb") as f: # open the file in binary read mode
        ftp.storbinary(f"STOR {filename}", f) # upload the file to the FTP server
    ftp.quit() # quit the FTP session

# main function
if __name__ == "__main__":
    start_time = time.time() # get the current time
    # loop for 2 hours
    while time.time() - start_time < 7200:
        # wait between 1 and 5 minutes before connecting to the FTP server
        time.sleep(random.randint(60, 300))
        # get the list of files in the FTP server directory
        files_dowload = list_files()
        files_upload =  list_file_upload()
        # choose a random file from the list
        
        # choose a random action (download or upload)
        action = random.choice(["download", "upload"])
        # download or upload the file
        if action == "download":
            filename = random.choice(files_dowload)
            download_file(filename)
        else:
            filename = random.choice(files_upload)
            upload_file(filename)
        # print the action and the file name
        print(f"{action} {filename}")