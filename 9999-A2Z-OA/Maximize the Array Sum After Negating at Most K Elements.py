"""Given an array A with only positive numbers. We are allowed to negate any entries in the array, (i.e set A[i] = -A[i]).
What is the maximum number of entries you can negate in the array such that every prefix sum after the negate operations is positive.

Example 1:

Input:  A = [4, 1, 1, 1]
Output: 3
Explanation:

We can apply only at-most 3 negate operations, to make A = [4, -1, -1, -1], after the negate operation,

The prefix sums of A, p(A) = [4, 3, 2, 1] which are all positive. So that the answer for A is 3.

counter = 1 update prefixSum with adding or subtracting
0 4 3
  4 1 1 1
    i
                      +  +
    A = [5,4,1, 1, 1, 1, 12 ]
         5 9 10 11 12 13 15
                       12 13


"""
## THIS IS A HARD PROBLEM !!!!!!!!!!!!!
## Also discussed here: https://codeforces.com/blog/entry/128417
## Explanation in detail: https://cfstep.com/training/tutorials/general-techniques/time-travel-in-greedy-algorithms/

## There is a similar and easy version on leetcode, just similar not the same
## https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/


from typing import List
import heapq



def func(nums:List[int]) -> int:
  pref = 0 #prefixSum
  heap = []
  heapq.heapify(heap)

  for n in nums:
    if pref >= n: # Negate this and insert into heap
      pref -= n
      heapq.heappush(heap,-n)
    else: # Can not negate this n, but maybe swith with a previous one
      if heap and (-heap[0]) > n:
        last = heapq.heappop(heap) * (-1)
        print(last)
        heapq.heappush(heap,-n)
        pref += (last) * 2
        pref -= n
      else:
        pref += n

  print(heap)
  return len(heap)

from Scripts.test_utils import test_case
test_case(func,([4,1,1,1],), 3)
test_case(func,([5,5,2, 2, 2, 2, 2],), 5)