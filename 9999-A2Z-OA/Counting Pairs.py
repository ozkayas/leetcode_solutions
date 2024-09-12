"""
https://www.fastprep.io/problems/amazon-count-pairs
Given an integer k and a list of integers, count the number of distinct valid pairs of integers (a, b)
 in the list for which 1 + k = b.
 Two pairs of integers (a, b) and (c, d) are considered dinstinct if at least one element
 of (a, b) does not also belong to (c, d).
 Note that the elements in a pair might be the same element in the array.
 An instance of this is below where k = 0.

Function Description

Complete the function countPairs in the editor.

countPairs has the following parameter(s):

int numbers[n]: array of integers
int k: target difference
Returns

int: number of valid (a, b) pairs in the numbers array that have a difference of k

Example 1:

Input:  numbers = [1, 1, 1, 2], k = 1
Output: 1
Explanation:

This arr has 3 different valid pairs: (1, 1), (1, 2), and (2, 2,).

For k = 1, there is only 1 valid pair which satisfies a + k = b: the pair (a, b) = (1, 2)

Input:  numbers = [1, 2], k = 0
Output: 2
Explanation:

This arr has 3 different valid pairs: (1, 1), (1, 2), and (2, 2,).

For k = 0, there is only 2 valid pair which satisfies a + k = b: 1 + 0 = 1 and 2 + 0 = 2.
"""
from typing import List

## 3 Methods looks reasonable
# 1. sorting and binary searching the pair, T = O(n log n) , S = O(1)
# 2. hash Map like 2 sum problem, T = O(n) S = (n)
# 3. sorting and 2 pointers, T = (n log n), S = O(1)

def countPairs(numbers:List[int], k:int) -> int:

    seen = set()
    counter = 0

    for n in numbers:
        # If already in list, prevent double counting
        if n in seen:
            continue

        seen.add(n)
        smallerPairOfN = n - k
        greaterPairOfN = n + k
        if smallerPairOfN in seen:
            counter += 1
        
        # smaller and greater pairs are distinct so check for both
        if k != 0 and greaterPairOfN in seen:
            counter += 1



    return counter

## 2. method using hash map
# def countPairs(numbers:List[int], k:int) -> int:
#     hMap = dict()
#     numbers = list(set(numbers)) # clean doubles
#     counter = 0

#     for n in numbers:
#         hMap[n] = True
    
#     for n in numbers:
#         if (n-k) in hMap:
#             counter += 1


#     return counter

from Scripts.test_utils import test_case
test_case(countPairs, ([3, 1, 4, 1, 5], 1), 2)
test_case(countPairs, ([3, 1, 4, 1, 5], 0), 4)
test_case(countPairs, ([1, 2], 0), 2)
test_case(countPairs, ([1, 1, 1, 2], 1), 1)