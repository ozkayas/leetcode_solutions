'''
Get Min Cost Data 🍊
🤘 INTERN
enthusiasts at Amazon are working on a data interpolation model to increase the size of the data set for better learning.

In one such model, there are 26 different classifications possible and the ith data point is annotated to belong to the data[i] class where data is a string of lowercase English letters. However, for some data points, data[i] is equal to '?' representing that the corresponding data point classification is missing and needs to be replaced with some lowercase English letter.

The cost of any index i of the string data is defined as the number of indices before it that also have the same classification result. For example,

For the string "hello" the costs are [0, 0, 0, 1, 0] corresponding to each index.
For the string "abc" the costs are [0, 0, 0] corresponding to each index.
For the string "aaccbbc" the costs are [0, 1, 0, 1, 0, 1, 2] corresponding to each index because before the last c character, there are 2 more c characters.
The task is to replace all the characters '?' so that the sum of the indices' cost is minimum.

Given the string data, interpolate the data such that the total cost of all the indices is minimized. If there are multiple ways to get minimum cost, print the lexicographically smallest possible string that satisfies the goal.

Function Description

Complete the function getMinCostData in the editor below.

getMinCostData has the following parameter:

data: a string
Returns

string: the lexicographically minimum string with the minimum cost

Note:

A string p is lexicographically smaller than string q, if p is a prefix of q, is not equal to q, or there exists i, such that pi < qi and for all j < i it is satisfied that pj = qj. Note that while comparing pj and qj we consider their ASCII values, i.e. '[' and ']' are greater than any uppercase English letters. For example, "ABC" is lexicographically smaller than "BCD" and "ABCD" but larger than "AAC" and "AACDE".
Example 1:

Input:  data = "aaaa?aaaa"
Output: "aaaabaaaa" 
Explanation:

Putting 'b' does not contribute to the total cost and is lexicographically minimum.
      
Example 2:

Input:  data = "??????"
Output: "abcdef" 
Explanation:

This is the lexicographically smallest string that keeps the cost least. The cost will be 0 as there will be no duplicate character present in it.
      
Example 3:

Input:  data = "abcd?"
Output: "abcde" 
Explanation:
'''

from collections import defaultdict
import heapq


def getMinCostData(data:str) -> str:
    freq = [0 for _ in range(26)]
    for ch in data:
        if ch != "?":
            idx = ord(ch) - ord("a")
            freq[idx] += 1

    minHeap = []
    for i, f in enumerate(freq):
        letter = chr(i + ord("a"))
        minHeap.append((f, letter))

    # minHeap = [(1,"a"),(0,"a"),(0,"b"),(1,"c"),(5,"d"),(0,"z")]
    heapq.heapify(minHeap)

    ans = []
    for i, ch in enumerate(data):
        if ch == "?":
            # get the first element with mincost and lexicog first
            count, letter = heapq.heappop(minHeap)
            ans.append(letter)
            # increase counter of this letter in the heap
            heapq.heappush(minHeap,(count +1, letter))

        else:
            ans.append(ch)


    return ''.join(ans)


print(getMinCostData("abcd?"))
print(getMinCostData("aaaa?aaaa"))
print(getMinCostData("?????"))
print(getMinCostData("a??bcd?"))