'''
https://www.fastprep.io/problems/amazon-maximum-user-traffic
In order to ensure a hassle-free user experience during the festive season, Amazon maintains logs of the days when its users use the Amazon Shopping app.

The user traffic of a day is said to be the maximum number of users logged into the application during that day. If a user uses the application from day login[i] to day logout[i], it increases the traffic of each day from login[i] to logout[i] (both inclusive) by 1. That is, if login[i] = 4 and logout[i] = 6, then this user increases the traffic of days 4, 5 and 6 by 1.

Given the login and logout day data of n users, find the number of days on which the user traffic is maximum.

Note that all logins take place before all logouts on a single day.

Function Description

Complete the function maximumUserTraffic in the editor below.

maximumUserTraffic has the following parameter(s):

int login[n]: an array of integers with login[i] denoting the login day of i^th user.
int logout[n]: an array of integers with logout[i] denoting the logout day of i^th user.
Returns

int: the number of days having maximum user traffic
'''
from typing import List

def maximumUserTraffic(login:List[int], logout:List[int]) -> int:
    N = len(login)
    maxSoFar, maxDayCount = 0, 0
    loggedIn = 0
    now, lastLogin= 0, 0

    login.sort()
    logout.sort()

    s, e = 0, 0

    # looping till the last logout
    while e < N:
        # a user logged in at time login[s]
        if s < N and login[s] < logout[e]:
            lastLogin = login[s]
            loggedIn += 1
                # If we hit a new maxForNow, reset daycount=1
            if loggedIn > maxSoFar:
                maxSoFar = loggedIn
                maxDayCount = 1
            elif loggedIn == maxSoFar:
                maxDayCount += 1
            # move pointer
            s += 1
        else:
            loggedIn -= 1
            # If loggedIn is just -1 than maxSoFar, just dropped from maxSoFar
            if loggedIn == maxSoFar-1:
                maxDayCount += (logout[e] - lastLogin)
            e += 1
        
    return maxDayCount




print(maximumUserTraffic([1, 2, 3],[10, 8, 4])) # output : 2
print(maximumUserTraffic([1, 2, 3, 7],[10, 9, 4 , 9])) # output : 2 + 3 = 5
print(maximumUserTraffic([1, 2, 3, 7],[10, 9, 5 , 9])) # output : 6