"""
https://www.fastprep.io/problems/amazon-find-unique-values
the experience points experience[i]. The company decided to pair the developers by iteratively pairing the developers with the highest and lowest remaining experience points for a hackathon. The combined experience of a pair is the average of the experience points of the two developers. Find the number of unique values among the combined experience of the pairs formed.

Function Description

Complete the function findUniqueValues in the editor below.

findUniqueValues has the following parameter:

int experience[n]: the experience points for each developer
Returns

int: the number of unique values among the combined experience points of the pairs formed

Example 1:

Input:  experience = [1, 4, 1, 3, 5, 6]
Output: 2
Explanation:

There are n = 6 developers. The pairs formed are (1, 6), (1, 5), and (4, 3) making their experience points 3.5, 3, and 3.5 respectively. There are 2 distinct values, 3 and 3.5, so return 2 as the answer.

Example 2:

Input:  experience = [1, 1, 1, 1, 1, 1]
Output: 1
Explanation:

The developers will be paired up as follows (by index): (0, 1), (2, 3), and (4, 5). Each pair has a combined experience of 1.

Example 3:

Input:  experience = [1, 100, 10, 1000]
Output: 2
Explanation:

The developers are paired as follows (by index): (0, 3), (1, 2). The pairs have combined experience points of 500.5, and 55 respectively.

Constraints:
1 <= n <= 105
n is an even number
1 <= esperience[i] <= 109
"""

from typing import List
from collections import deque

def findUniqueValues(exp: List[int]) -> int:
    exp.sort()
    first, last = 0, len(exp)-1
    expSet = set()

    while first < last:
        pairTotalExp = exp[first] + exp[last]
        expSet.add(pairTotalExp)
        first += 1
        last -= 1

    print(expSet)
    return len(expSet)


print(findUniqueValues([1, 4, 1, 3, 5, 6]))
print(findUniqueValues([1, 1, 1, 1, 1, 1]))
print(findUniqueValues([1, 100, 10, 1000]))