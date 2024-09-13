"""
https://leetcode.com/discuss/interview-question/2688170/New-OA-Question%3A-Bags-of-Rice

You are shopping on Amazon.com for some bags of rice. Each listing displays the number of grains of rice that the bag contains. You want to buy a perfect set of rice bags. From the entire search results list, riceBags. A perfect set of rice bags, perfect, is defined as:

The set contains at least two bags of rice.
When the rice bags in the set perfect are sorted in increasing order by grain count, it satisfies the condition perfect[i] * perfect[i] = perfect[i+1] for all 1 ≤ i < n. Here perfect[i] is the size of the set and perfect[i] is the number of rice grains in bag i.
Find the largest possible set perfect and return an integer, the size of that set. If no such set is possible, then return -1. It is guaranteed that all elements in riceBags are distinct.

Function Description

Complete the function maxSetSize in the editor.

maxSetSize has the following parameter:

int riceBags[n]: the list of bags of rice by rice grain counts
Returns

int: the size of the largest set possible or -1 if there is none

Example 1:

Input:  riceBags = [625, 4, 2, 5, 25]
Output: 3
Explanation:

All of the possible perfect sets:

- [625, 25]
- [4, 2]
- [5, 25]
- [625, 5, 25]
The largest perfect set has size 3.

Example 2:


Input:  riceBags = [3, 9, 4, 2, 16]
Output: 3
Explanation:

Let the bags of rice available on Amazon have grain counts [3, 9, 4, 2, 16]. The following are the perfect sets:

Set perfect = [3, 9]. The size of this set is 2.
Set perfect = [4, 2]. The size of this set is 2.
Set perfect = [4, 16]. The size of this set is 2.
Set perfect = [4, 2, 16]. The size of this set is 3.

The size of the largest set is 3.
The image above illustrates the correct ordering of the purchased rice bags by grains of rice.

Constraints:
1 ≤ n ≤ 2 × 105
2 ≤ riceBags[i] ≤ 106
"""
from typing import List


def maxSetSize(bags: List[int]) -> int:
    isSeen = {bag:False for bag in bags}
    maxLength = 0

    for bag in bags:
        length = 0

        if bag in isSeen and not isSeen[bag]:
            isSeen[bag] = True
            length += 1

            # move forward
            next = pow(bag, 2)
            while next in isSeen and  not isSeen[next]:
                isSeen[next] = True
                length += 1
                next = pow(next, 2)

            # move backwards
            prev = pow(bag, 0.5)
            while prev in isSeen and  not isSeen[prev]:
                isSeen[prev] = True
                length += 1
                prev = pow(prev, 0.5)

        maxLength = max(maxLength, length)

    return maxLength

    # # Try to find a minimum of a sequence
    # for bag in bagSet:
    #     counter = 0
    #     if pow(bag, 0.5) not in bagSet: # we found a beginning of a seri
    #         cur = bag
    #         while cur in bagSet:
    #             counter += 1
    #             cur = pow(cur, 2)

    #         possibleCountedSets.append(counter)
    
    # return max(possibleCountedSets)



print(maxSetSize([3, 9, 4, 2, 16]))
print(maxSetSize([3, 9, 4, 2, 16, 256, ]))
print(maxSetSize([625, 4, 2, 5, 25, 1, 16, 256]))

