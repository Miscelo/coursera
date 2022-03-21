#!/usr/bin/env python3

import os
import shutil
import sys

# ************************************
# ******  Script to ask for username




def check_reboot():
    return os.path.exists("/run/reboot-required")


#Function that returns username
def getUsername():
    user = input("Choose username please: ")
    return user

#write user to file with all users included
def usernameToDBase():
    username = getUsername()
    with open("users.txt", 'a') as f:
        f.write(username + "\n")
    f.close()




if __name__ == '__main__':
    usernameToDBase()
