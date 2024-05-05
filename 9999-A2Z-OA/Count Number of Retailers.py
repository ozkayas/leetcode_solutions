'''
https://www.fastprep.io/problems/amazon-count-number-of-retailers

In a newly planned city, where a city is located at each integral coordinate in a 2-dimensional plane, there are n Amazon retailers. The ith retailer residing in the city at the coordinate (x[i], y[i]) and can deliver to all the cities covered by the rectangle having the 4 corner points (0, 0), (x[i], 0), (0, y[i]), (x[i], y[i]). We say that a point (a, b) is covered by a rectangle if it lies inside the rectangle or on its boundaries. Note that no 2 retailers reside in the same city.

Given q requests of the form (a, b), determine the number of retailers who can deliver to the city at the coordinate (a, b).

Function Description

Complete the function countNumberOfRetailers in the editor.

countNumberOfRetailers has the following parameter(s):

int retailers[n][2]: the retailers' coordinates
int requests[q][2]: the coordinates of cities to deliver to
Returns

int array[q]: the jth element is the answer to the jth query

Example 1:

Input:  retailers = [[1, 2], [2, 3], [1, 5]], requests = [[1, 1], [1, 4]]
Output: [3, 1] 
Explanation:
'''
from typing import List

# Returns first retailer (sorted) that covers this request
def binarySearchX(retailers: List[List[int]], request:List[int]) -> int:
    l, r = 0, len(retailers)-1

    # The index of the first retailer in the X coord sorted retailers.
    firstX = 0

    while l <= r:
        m = l + (r - l) // 2

        if request[0] <= retailers[m][0]:
            # We are ok, this retailer can cover, but try to find a smaller one on left
            firstX = m
            r = m - 1
        else:
            l = m + 1

    return firstX

# Returns first retailer (sorted) that covers this request
def binarySearchY(retailers: List[List[int]], request:List[int]) -> int:
    l, r = 0, len(retailers)-1

    # The index of the first retailer in the X coord sorted retailers.
    firstX = 0

    while l <= r:
        m = l + (r - l) // 2

        if request[1] <= retailers[m][1]:
            # We are ok, this retailer can cover, but try to find a smaller one on left
            firstX = m
            r = m - 1
        else:
            l = m + 1

    return firstX



def countNumberOfRetailers(retailers: List[List[int]], requests: List[List[int]]) -> List[int]:
    retailers.sort(key = lambda item: (item[0]))
    ans = []

    for req in requests:
        firstX = binarySearchX(retailers, req)
        targetRetails = retailers[firstX:]
        targetRetails.sort(key=lambda item:(item[1]))
        firstY = binarySearchY(targetRetails,req)

        ans.append(len(targetRetails) - firstY)
    return ans





print(countNumberOfRetailers([[1, 2], [2, 3], [1, 5]], [[1, 1], [1, 4]]))
print(countNumberOfRetailers([[1, 2], [2, 3], [1, 5], [1,1]], [[1, 1], [1, 4]]))