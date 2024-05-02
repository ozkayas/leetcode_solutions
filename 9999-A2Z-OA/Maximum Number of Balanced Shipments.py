'''
https://www.fastprep.io/problems/amazon-maximum-number-of-shipments
Amazon has multiple delivery centers for the distribution of its goods. 
In one such center, parcels are arranged in a sequence where the ith parcel has a weight of weight[i].
A shipment is constituted of a contiguous segment of parcels in this arrangement. 
That is, for 3 parcels arranged with weights [3, 6, 3] a shipment can be formed of parcels 
with weights [3], [6], [3], [3, 6], [6, 3] and [3, 6, 3] but not with weights [3, 3]. 
These shipments are to be loaded for delivery and must be balanced.

A shipment is said to be balanced if the weight of the last parcel of the shipment is not the maximum weight 
among all the weights in that shipment. For example, shipment with weights [3, 9, 4, 7] is balanced 
since the last weight is 7, while the maximum shipment weight is 9. However, the shipment [4, 7, 2, 7] is not balanced.

Given the weights of n parcels placed in a sequence, 
find the maximum number of shipments that can be formed such that each parcel belongs to exactly one shipment, 
each shipment consists of only a contiguous segment of parcels, and each shipment is balanced. 
If there are no balanced shipments, return 0.

Function Description

Complete the function maxNumberOfBalancedShipments in the editor.

maxNumberOfBalancedShipments has the following parameter:

int[] weights: an array of integers representing the weights of the parcels
Returns

int: the maximum number of balanced shipments that can be formed

Example 1:

Input:  weights = [1, 2, 3, 2, 6, 3]
Output: 2 
Explanation:

There are n = 6 parcels to ship. The parcels can be divided into two shipments:

[1, 2, 3, 2] and [6, 3]

each of which is balanced.

It can also be shown that this is the max num of shipments that can be formed. Thus, the answer is 2.

      
Example 2:

Input:  weights = [8, 5, 4, 7, 2]
Output: 2 
Explanation:

Form balanced shipments as [[8, 5], [4, 7, 2]] or [[8, 5, 4], [7, 2]]. In either case, the max num of shipments is 2.
      
Example 3:

Input:  weights = [4, 3, 6, 5, 3, 4, 7, 1]
Output: 3 
Explanation:

Some ways to form balanced shipments are:

[[4, 3, 6, 5], [3, 4, 7, 1]] or

[[4, 3], [6, 5,], [3, 4, 7, 1]] or

[[4, 3, 6, 5, 3], [4, 7, 1]].

It is not possible to form more than 3 balanced shipments. So the ans is 3.
      
Constraints:
1 <= n <= 105
1 <= weight[i] <= 109
'''
from typing import List

def maxNumberOfBalancedShipments(weight:List[int]) -> int:
    mono_stack = []
    counter = 0
    maxInStackSoFar = weight[0]

    for w in weight:
        # If stack is empty start a new shipment
        mono_stack.append(w)
        maxInStackSoFar = max(maxInStackSoFar, w)

        if mono_stack[-1] < maxInStackSoFar:
            # last added is smaller than maxSoFar, so we can greedyly add a new shipment
            counter += 1
            maxInStackSoFar = 0
            mono_stack.clear()
    
    if len(mono_stack) > 0:
        return 0
    else:
        return counter


print(maxNumberOfBalancedShipments([1, 2, 3, 2, 6, 3])) # output: 2
print(maxNumberOfBalancedShipments([8, 5, 4, 7, 2])) # output: 2
print(maxNumberOfBalancedShipments([4, 3, 6, 5, 3, 4, 7, 1])) # output: 3
print(maxNumberOfBalancedShipments([4, 3, 6, 5, 3, 4, 7, 7])) # output: 0