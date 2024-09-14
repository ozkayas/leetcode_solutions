"""
Given lots of intervals of login and logout of users, find maximum rush happened.
example:
login: [1,5,5]
logout: [5,10,5]

maximum rush happened at 5 and it happened thrice. So answer is 3

login: [4,10]
logout: [8,20]
maximum rush is 1 in those two interval. Hence answer is 16 = 8-4+1 + 20-10+1
"""

### The trick is adding 1 to the logout time to make sure the logout time is included in the rush time

from collections import defaultdict
from typing import List
def maxRush(login:List[int], logout:List[int]) -> int:


    n = len(login)
    # Create a list of tuples with the time and the operation type, 0 for login and 1 for logout
    # using 0 and 1 because login time comes before the logout time
    login = [(login[i], 0) for i in range(n)]
    logout = [(logout[i]+1, 1) for i in range(n)]
    all = sorted(login + logout)
    loggedIn = 0
    prevOperationTime = 0

    # Will hold rush and the time
    rushMap = defaultdict(int)
    # maxRush = 0
    for i in range(len(all)):

        rushMap[loggedIn] += all[i][0] - prevOperationTime

        if all[i][1] == 0:
            loggedIn += 1
        else:
            loggedIn -= 1
        prevOperationTime = all[i][0]

    maxLoggedIn = max(rushMap.keys())
    return maxLoggedIn * rushMap[maxLoggedIn]


print(maxRush([5], [5])) #1
print(maxRush([1,5,5], [5,10,5])) #3
print(maxRush([4, 10], [8, 20])) #16