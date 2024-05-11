'''
Find Maximum Maxima Count 🍊
🔥 FULLTIME
Amazon has a string of categories of items purchased by a particular customer, each represented as a lowercase English letter. To analyze customer behavior, we define a metric called the MaximumCount of a category. It is the number of indices where the frequency of some category c is maximum among all categories present in the prefix.

More elaboratively, MaximumCount of character, char, representing a category is defined as the number of indices i, such that the frequency of char is maximal in the prefix of the string up to the index i.

Given the string categories, find the maximum MaximumCount among all the categories.

Function Description

Complete the function findMaximumMaximumCount in the editor.

findMaximumMaximumCount has the following parameter:

string categories: the given string
Returns

int: the maximum MaximumCount

Example 1:


Input:  categories = "bccaaacb"
Output: 6 
Explanation:

From the above table (assuming 1-based indexing):

MaximaCount of a = 4 at indices 5, 6, 7, 8

MaximaCount of b = 2 at indices 1, 2

MaximaCount of c = 6 at indices 2, 3, 4, 5, 7, 8


Thus the maximum MaximaCount is 6 for the character c.
'''

from collections import defaultdict
from heapq import heappop, heappush

def findMaximumMaximumCount(categories) -> int:
    # holds the freq of each letter at the time of loop, will push this to heap for cur letter while looping
    freq = [0 for i in range(26)]
    maximas = defaultdict(int)
    maxHeap = []

    def updateMaximas(heap):
        temp = []
        maxValue = -heap[0][0]
        while heap and -heap[0][0] == maxValue:
            val, ch = -heap[0][0] , heap[0][1]
            maximas[ch] += 1
            temp.append((val, ch))
            heappop(heap)
        for val, ch in temp:
            heappush(heap, (-val, ch))
    
    for ch in categories:
        chIndex = ord(ch)-ord('a')
        freq[chIndex] += 1
        heappush(maxHeap, (-freq[chIndex], ch)) 
        updateMaximas(maxHeap)

    return max(maximas.values())

print(findMaximumMaximumCount("bccaaacb"))
print(findMaximumMaximumCount("adbcbcbcc"))
print(findMaximumMaximumCount("zzzz"))
        
