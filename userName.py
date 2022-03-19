#!/usr/bin/env python3

#********************************************
#Script to ask for username
#********************************************




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
