'''
https://www.fastprep.io/problems/amazon-find-min-trips
Find Minimum Trips
There were a large number of orders placed on Amazon Prime Day. 
The orders are packed and are at the warehouse ready to be delivered. 
The delivery agent needs to deliver them in as few trips as possible.

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
The agent needs a min of 3 trips as shown above. Return 3 as the answer :)
      
Constraints:
1 ≤ n ≤ 1055
1 ≤ packageweight[i] ≤ 109
'''
from typing import List
from collections import Counter

def decreaser(n: int) -> int:
    if n % 3 == 0: return n // 3

    counter = 0

    while n > 0:
        if n >= 3:
            n -= 3
            counter += 1
        if n == 2:
            n -= 2
            counter += 1

    return counter  

def findMinTrips(arr: List[int]) -> int:
    freq = Counter(arr)
    trips = 0

    for k, v in freq.items():
        if v < 2:
            return -1
        else:
            trips += decreaser(v)

    return trips

print(findMinTrips([1, 8, 5, 8, 5, 1, 1])) # 3
print(findMinTrips([3, 4, 4, 3, 1])) # -1
print(findMinTrips([2, 4, 6, 6, 4, 2, 4])) # 3