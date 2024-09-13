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
from collections import defaultdict
from typing import List
def maxRush(login:List[int], logout:List[int]) -> int:


    n = len(login)
    # Create a list of tuples with the time and the operation type, 0 for login and 1 for logout
    # using 0 and 1 because login time comes before the logout time
    login = [(login[i], 0) for i in range(n)]
    logout = [(logout[i], 1) for i in range(n)]
    all = sorted(login + logout)
    loggedIn = 0
    prevOperationTime = 0

    # Will hold rush and the time
    rushMap = defaultdict(int)
    # maxRush = 0
    for i in range(len(all)):

        rushMap[loggedIn] += all[i][0] - prevOperationTime +1

        if all[i][1] == 0:
            loggedIn += 1
        else:
            loggedIn -= 1
        prevOperationTime = all[i][0]


    return max(rushMap.values())

print(maxRush([5], [5])) #3
print(maxRush([1,5,5], [5,10,5])) #3
print(maxRush([4, 10], [8, 20])) #16


# Program to find maximum guest
# at any time in a party
def findMaxGuests(arrl, exit):
    n = len(arrl)
    # Sort arrival and exit arrays
    arrl.sort()
    exit.sort()

    # guests_in indicates number of
    # guests at a time
    guests_in = 1
    max_guests = 1
    time = arrl[0]
    i = 1
    j = 0

    # Similar to merge in merge sort to
    # process all events in sorted order
    while i < n and j < n:

        # If next event in sorted order is
        # arrival, increment count of guests
        if arrl[i] <= exit[j]:


            guests_in = guests_in + 1

            # Update max_guests if needed
            if guests_in > max_guests:
                max_guests = guests_in
                time = arrl[i]

            # increment index of arrival array
            i = i + 1

        else:
            guests_in = guests_in - 1
            j = j + 1

    print("Maximum Number of Guests =",
          max_guests, "at time", time)

# findMaxGuests([1, 2, 10, 5, 5], [4, 5, 12, 9, 12] )
# findMaxGuests([1,5,5,5], [5,5,10,6] )
# findMaxGuests([4, 10], [8, 20] )
