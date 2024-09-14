"""
Calculate Beauty Values
📚
RELATED PROBLEMS
Given an array arr of size n and pairs of size m * 2, where each pair represents the starting and ending index of a subarray, we need to calculate the beauty of the array. The process of calculating the beauty involves creating a beautiful array by processing each pair and appending the subarray defined by the pair to the beautiful array. After processing all pairs, we need to return the summation of the count of values exactly lesser than the values at the unused indexes in the original array.

Function Description

Complete the function calculateBeautyValues in the editor.

calculateBeautyValues has the following parameters:

1. int arr[n]: an array of integers
2. int pairs[m][2]: an array of pairs representing subarray indexes
Returns

int: the sum of counts of values less than the values at unused indexes

Example 1:

Input:  arr = [1, 2, 3, 2, 4, 5], pairs = [[0, 1], [3, 4], [0, 0], [3, 4]]
Output: 12
Explanation:


The process of creating the beautiful array is as follows:




Process pair 0-1: beautiful array becomes [1, 2]


Process pair 3-4: beautiful array becomes [1, 2, 2, 4]


Process pair 0-0: beautiful array becomes [1, 2, 2, 4, 1]


Process pair 3-4: beautiful array becomes [1, 2, 2, 4, 1, 2, 4]



The final beautiful array is [1, 2, 2, 4, 1, 2, 4]. The unused indexes in the original array are 2 and 5,

with values 3 and 5 respectively. In the beautiful array, there are 5 values lesser than 3 and 7 values

lesser than 5, so the count is 5 + 7 = 12. Therefore, the final answer is 12.
"""
from bisect import bisect_left
from collections import defaultdict
from email.policy import default


def calculateBeautyValues(arr, pairs) -> int:
    unusedIndexes = set(range(len(arr)))
    # Holds the frequency of each element in the array
    freq = defaultdict(int)

    for pair in pairs:
        subArray = arr[pair[0]:pair[1]+1]
        # Update the unused indexes
        unusedIndexes -= set(range(pair[0], pair[1]+1))
        for element in subArray:
            freq[element] += 1
    print(unusedIndexes)
    print(freq.items())

    # Calculate prefix Sum of freq.items()
    preSumFreq = []
    sm = 0
    for key, value in freq.items():
        sm += value
        preSumFreq.append((key, sm))
    print(preSumFreq)


    # Calculate the sum of counts of values less than the values at unused indexes
    # using bisectleft
    count = 0
    for index in unusedIndexes:
        # use bisectleft to find the index of the first element greater than arr[index]
        targetIndex = bisect_left(preSumFreq, (arr[index],0)) - 1
        count += preSumFreq[targetIndex][1]

    return count



print(calculateBeautyValues([1, 2, 3, 2, 4, 5], [[0, 1], [3, 4], [0, 0], [3, 4]]) )