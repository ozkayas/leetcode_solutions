'''
Same leetcode problem:


2. Items in Containers
Amazon would like to know how much inventory exists in their closed inventory compartments. Given a string s consisting of items as "* and closed compartments as an open and close " " an array of starting indices startindices, and an array of ending indices endindices, determine the number of items in closed compartments within the substring between the two indices, inclusive.

An item is represented as an asterisk ('*'= ascii decimal 42)
A compartment Is represented as a pair or pipes that may or may not have items between them ('I'= ascii decimal 124)
Example
S= '|**|*|*'
startindices = [1, 1]
endindices = [5, 6]

The string has a total of 2 closed compartments, one with 2 items and one with 1 item. For the first pair of indices, (1, 5), the substring is '|**|*'There are 2 items in a compartment
For the second pair of indices, (1, 6), the substring is '|**|*|*' and there are 2 + 1 = 3 items in compartments.
Both of the answers are returned in an array [2,3]

Function Description.
Complete the numberOfitems function in the editor below. The function must return an integer arrav that contains the results for each of the startIndices[i] and endindices(i] pairs.

numberOfltems has three parameters:

S: A string to evaluate
startindices: An integer arrav, the starting indices
endindices: An integer array, the ending indices.
Constraints

1 <= m, n <= 10^5
1 <= startindices[i] <= endindices[i] <= n
Each character of s is either '*' or '|'
Sample Input 1

S = '*|*|'
startIndices = [1]
endIndices = [3]
Sample Output 1

0
Explanation
The substring from index = 1 to index = 3 is '*|*' There is no compartments In this string

Sample Input 2

S = '*|*|*|'
startIndices = [1]
endIndices = [6]
Sample Output 2

2
Explanation
The substring from index = 1 to index = 3 is '*|*|*|' There are two compartments in this string at (index = 2, index = 4) and (index = 4, index = 6). There are 2 items between these compartments.
'''

from collections import deque
from collections import defaultdict

def bfs(n, m, edges, s):
    levels = [-1 for _ in range(n+1)]
    
    adj_list = defaultdict(list)
    for k, v in edges:
        adj_list[k].append(v)
    
    # print("adj", adj_list)
    stack = deque() # Stack will hold val, level
    stack.append((s, 0))
    
    # Start bfs
    while stack:
        node, level = stack.popleft()
        levels[node] = level
        for child in adj_list[node]:
            stack.append((child, level+1))
        
    ans = []
    for level in levels:
        if level > 0:
            ans.append(level * 6)
        if level == -1:
            ans.append(level)
    return ans[1:]