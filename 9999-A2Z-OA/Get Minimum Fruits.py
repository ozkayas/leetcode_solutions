"""
https://www.fastprep.io/problems/get-minimum-fruits
Amazon recently launched a new game, Fruit Crush! In this game, you are allowed to choose two dissimilar fruits and crush them. Each type of fruit is represented as an integer in an array. Formally you can choose any two unequal integers in the array and delete them.

Given an array fruits of size n, return the minimum possible number of fruits left after the given operation is performed any number of times.

Function Description

Complete the function getMinimumFruits in the editor.

getMinimumFruits has the following parameter(s):

int fruits[n]: array of n fruits
Returns

int: the minimum possible count of fruits left

Input:  fruits = [3, 3, 1, 1, 2]
Output: 1
Explanation:


Fruit 1 (banana) and 2 (pineapple) can be crushed first, followed by numbers 1(banana) and 3 (orange). Only 3 (orange) remains in the array, hence the answer is 1.

Example 2:

Input:  fruits = [1, 2, 5, 6]
Output: 0
Explanation:


Fruit 1 and 2 can be taken and fruit 5 and 6 can be taken. Hence no numbers are left.

Constraints:
1 <= n <= 105
1 <= fruits[i] <= 109

fruits = [1,1,1,1,1,1,1,1,1,1, 2,2,2,2,2, 5,5, 6]
[30,25,12,4,2]
"""
from typing import List
import collections
import heapq


def getMinimumFruits(fruits: List[int]) ->int:
    
    # We only need to check frequencies, fruits themselves are not needed
    # We willuse a max heap, to get max 2 freq, crush them and put back, then do the same again until heap lenght <= 1
    freqOfFruits = [(freq * -1) for freq in list((collections.Counter(fruits)).values())]
    heapq.heapify(freqOfFruits)

    while len(freqOfFruits) > 1:
        # Get the most frequest 2 fruits
        first = heapq.heappop(freqOfFruits)*-1
        second = heapq.heappop(freqOfFruits)*-1
        

        #crush them 
        remaining = abs(first - second)
        if remaining > 0:
            heapq.heappush(freqOfFruits, -1 * remaining)
        # print(first, second, remaining, freqOfFruits)

    if len(freqOfFruits) == 0:
        return 0
    if len(freqOfFruits) == 1:
        return freqOfFruits[0] * -1
    else:
        return abs(freqOfFruits[0]-freqOfFruits[1])


print(getMinimumFruits([3, 3, 1, 1, 2])) #1
print(getMinimumFruits([1, 2, 5, 6])) #0
print(getMinimumFruits([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,5,5,5,5,5,5,5,5,5,5,5,5,6,6,6,6,7,7]))
