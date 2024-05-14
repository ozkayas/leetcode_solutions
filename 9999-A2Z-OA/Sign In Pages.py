'''
Notes:

Initially, there are no users registered.
If a user is already logged in and makes a login request, the new request is unsuccessful. The original login remains active.
Each log is an API request and is in one of the three allowed formats.
The order of execution of each requests is the same as order of the input.
The username and passwords are case-sensitive.
Function Description

Complete the function signInPages in the editor.

signInPages has the following parameter:

String[] requests: an array of API requests
Returns

String[]: an array of responses for each API request

Example 1:

Input:  requests = ["register david david123", "register adam 1Adam1", "login david david123", "login adam 1adam1", "logout david"]
Output: ["Registered Successfully", "Registered Successfully", "Logged In Successfully", "Login Unsuccessful", "Logged Out Successfully"] 
'''
from typing import List

def signInPages(requests:List[str]) -> List[str]:
    userDB = dict()
    onlineUsers = set()

    regSuc = "Registered Successfully"
    userExists = "Username Already Exists"
    logInSuc = "Logged In Successfully"
    logInUn = "Login Unsuccessful"
    logoutSuc = "Logged Out Successfully"
    logoutUn = "Logout Unsuccessful"

    output = []
    
    for req in requests:
        reqList = req.split(" ")
        if len(reqList) == 3:
            operation, username, password = reqList[0], reqList[1], reqList[2]
        else:
            operation, username = reqList[0], reqList[1]

        if operation == "register":
            if username in userDB:
                output.append(userExists)
            else:
                userDB[username] = password
                output.append(regSuc)

        elif operation == 'login':
            if username not in userDB or userDB[username] != password:
                output.append(logInUn)
            elif username in onlineUsers:
                output.append(logInUn)
            else:
                onlineUsers.add(username)
                output.append(logInSuc)

         
        else:
            if username in onlineUsers:
                output.append(logoutUn)
            else:
                output.append(logoutSuc)


    return output


print(signInPages(["register david david123", "register adam 1Adam1", "login david david123", "login adam 1adam1", "logout david"]))











