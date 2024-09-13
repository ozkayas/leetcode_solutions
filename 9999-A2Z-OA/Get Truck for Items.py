'''
https://www.fastprep.io/problems/get-trucks-for-items

Amazon Warehouse delivers different items in different trucks having varied capacities.

Given an array, trucks, of n integers that represents the capacities of different trucks, and an array, items, of m integers that represent the weights of different items, for each item, find the index of the smallest truck which has a capacity greater than the item's weight. If there are multiple such trucks, choose the one with the minimum index.

If there is no truck that can carry the item, report -1 as the answer for the corresponding item.

Note: Assume that the trucks are indexed starting from 0. Also, multiple items can be mapped to the same truck. Each item is mapped independently, hence the trucks do not lose any capacity when a particular item is mapped to it.

Function Description

Complete the function getTrucksForItems in the editor below.

getTrucksForItems has the following parameters:

int trucks[n]: the capacities of the trucks
int items[m]: the weights of the items
Example 1:


Input:  trucks = [4, 5, 7, 2], items = [1, 2, 5]
Output: [3, 0, 2] 
Explanation:

Given the above trucks and items, they can be mapped as the image shows. The smallest truck that can carry the third weight, 5, is truck 2 with a capacity of 7. Similar logic is applied to the other elements and the answer is [3, 0, 2].
Example 2:

Input:  trucks = [5, 3, 8, 1], items = [6, 10]
Output: [2, -1] 
Example 3:

Input:  trucks = [1, 3, 5, 2, 3, 2], items = [1, 2, 3]
Output: [3, 1, 2] 
Explanation:


1. items[0] = 1, 2 is the samllest value in the array greater than 1. trucks[3] and trucks[5] are equal to 2. The minimum index among them is 3.

2. items[1] = 2, 3 is the smallest value in the array greater than 2. trucks [1] and trucks[4] are equal to 3. The minimum index among them is 1.

3. items[2] = 3, 5 is the smallest value in the array greater than 3. trucks[2] is equal to 5.
      
Constraints:
1 ≤ n ≤ 105
1 ≤ trucks[i] ≤ 109
1 ≤ m ≤ 105
1 ≤ items[m] ≤ 109
'''
from bisect import bisect, bisect_left
from typing import List

def getTrucksForItems(trucks, items) -> List[int]:
    # create truck list with index, sorted
    arr = sorted([(trucks[i], i) for i in range(len(trucks)) ], key= lambda i:(i[0], i[1]))
    # print(arr)
    ans = []
    for item in items:
        index = bisect_left(arr, item+1, key= lambda i:i[0])
        if 0 <= index < len(arr):
            ans.append(arr[index][1])
        else:
            ans.append(-1)
    return ans

print(getTrucksForItems([4, 5, 7, 2],  [1, 2, 5]))
print(getTrucksForItems([5, 3, 8, 1], [6, 10]))
print(getTrucksForItems([1, 3, 5, 2, 3, 2], [1, 2, 3]))