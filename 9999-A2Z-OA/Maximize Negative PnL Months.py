"""
https://www.fastprep.io/problems/amazon-maximize-negative-pnl_months

You are analyzing the market trends of Amazon stocks. An AWS financial service model returned an array of integers, PnL (Profit and Loss), for your portfolio representing that in the ith month, you will either gain or lose PnL[i]. All reported PnL values are positive, representing gains.

As part of the analysis, you will perform the following operation on the PnL array any number of times:

Choose any month (0 ≤ i < n) and multiply PnL[i] by -1
Find the maximum number of months you can afford to face a loss, i.e., have a negative PnL, such that the cumulative PnL for each of the n months remains strictly positive i.e. remains greater than 0.

Note: The cumulative PnL for the ith month is defined as the sum of PnL from the starting month up to the ith month. For example, the cumulative PnL for the PnL = [3, -2, 5, -6, 1] is [3, 1, 6, 0, 1].

Function Description

Complete the function maximizeNegativePnLMonths in the editor.

maximizeNegativePnLMonths has the following parameter:

int[] PnL: an array of integers representing the Profit and Loss for each month
Returns

int: the maximum number of months with a negative PnL such that the cumulative PnL remains positive
Example 2:

Input:  PnL = [1, 1, 1, 1, 1]
Output: 2
Explanation:

There are multiple possible PnLs such as [1, -1, -1, 1, 1], [-1, 1, -1, 1, -1], etc.

However, it is optional to modify the PnL to be [1, 1, -1, 1, -1] or [1, 1, 1, -1, -1].

Example 3:

Input:  PnL = [5, 2, 3, 5, 2, 3]
Output: 3
Explanation:

The possible PnLs such that all the cumulative PnLs are positive are:

[5, 2, -3, 5, 2, -3]

[5, 2, 3, 5, -2, -3]

[5, -2, 3, 5, -2, -3]

etc...

The max num of negatives we can have ensuring that all the culmulative PnLs are positive is 3 corresponding to the case [5, -2, 3, 5, -2, -3].

Note that [5, 2, 3, -5, -2, -3] is not a valid case as the culative PnLs are [5, 7, 10, 5, 2, 0] but they must be strictly positive.


Constraints:
1 <= n <= 10
1 <= PnL[i] <= 109

"""
from typing import List
import heapq

def maximizeNegativePnLMonths(pnl: List[int]):
    # Will use this to time travel and reverse a negated value
    maxHeap = []
    heapq.heapify(maxHeap)

    N = len(pnl)
    count = 0
    pSum = 0

    # I will try a greedy approach with a heap to switch with a past value
    for i in range(N):
        if pnl[i] <= pSum: # We can negate this month
            pSum -= pnl[i]
            count += 1
            # add negated value to the heap, for later if needed to change
            heapq.heappush(maxHeap, -pnl[i])
        else:
            # Maybe there is a bigger negated value and we can switch it with this one
            if maxHeap and ( pSum - 2* maxHeap[0] ) > pnl[i]:
                item_to_reverse = -heapq.heappop(maxHeap)
                pSum += 2 * item_to_reverse
                pSum -= pnl[i]
                heapq.heappush(maxHeap, -pnl[i])
            else:
                pSum += pnl[i]
        # print(maxHeap)
    return count
    
pnl = [1,1,5,2,4,2,3,4,5,5]
print(maximizeNegativePnLMonths(pnl))
# pnl = [5, 3, 1, 2]
# print(maximizeNegativePnLMonths(pnl))


'''
0 5 2 1
5 3 1 2
    ^
  c =2

'''



'''
 3   1  6  12  11
[3, -2, 5, 6, -1]
           |
 5  2   1 
[5, -3, -1,  2]
            |
'''