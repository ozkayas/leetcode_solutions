'''
Find Minimum Trips 🍌
🤘 INTERN
There were a large number of orders placed on Amazon Prime Day. The orders are packed and are at the warehouse ready to be delivered. The delivery agent needs to deliver them in as few trips as possible.

In a single trip, the delivery agent can choose packages following either of two rules:

Choose two packages with the same weight
Choose three packages with the same weight
Determine the minimum number of trips required to deliver the packages. If it is not possible to deliver all of them, return -1.

Function Description

Complete the function findMinTrips in the editor.

findMinTrips has the following parameter:

int packageweight[n]: the weights of each package
Returns

int: the minimum number of trips required or -1 if it is not possible to deliver them all

𓆝 𓆟 𓆞 🐰 Credit to Jane 🐰 𓆝 𓆝 𓆟

Example 1:


Input:  packageweight = [1, 8, 5, 8, 5, 1, 1]
Output: 3 
Explanation:

It takes 3 trips to deliver all the packages.
      
Example 2:

Input:  packageweight = [3, 4, 4, 3, 1]
Output: -1 
Explanation:

Packages with weights 3 and 4 can be removed in groups of two. The package of weight 1 cannot be delivered as it cannot be chosen according to the rules. Since it is not possible to deliver all packages, the answer is -1.
      
Example 3:


Input:  packageweight = [2, 4, 6, 6, 4, 2, 4]
Output: 3 
Explanation:

The agent needs a min of 3 trips as shown above. 
'''
from collections import defaultdict
from typing import List

def findMinTrips(pW: List[int]) -> int:
    trips = 0
    freq = defaultdict(int)
    for num in pW:
        freq[num] += 1
    
    for num, count in freq.items():
        while count > 0:
            if count >= 3:
                trips += 1
                count -= 3
            elif count == 2:
                trips += 1
                count -= 2
            else:
                return -1

    return trips


print(findMinTrips([1, 8, 5, 8, 5, 1, 1]))
print(findMinTrips([3, 4, 4, 3, 1]))
print(findMinTrips([2, 4, 6, 6, 4, 2, 4]))