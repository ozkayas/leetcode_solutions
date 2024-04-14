'''An AWS client wants to deploy multiple applications and needs two servers, one for their frontend and another for their backend. They have a list of integers representing the quality of servers in terms of availability. The client's preference is that the availability of an application's frontend server must be greater than that of its backend.

Two arrays of same size n, frontend[n] and backend[n] where elements represent the quality of the servers, create pairs of elements (frontend[i], backend[i]) such that frontend[i] > backend[i] in each pair. Each element from an array can be picked only once to form a pair, Find the maximum number pairs that can be formed.

Function Description

Complete the function getMaxPairs in the editor.

getMaxPairs has the following parameters:

int frontend[n]: frontend server qualities
int backend[n]: backend server qualities
Returns

int: the maximum number of pairs that can be formed

Example 1:

Input:  frontend = [1, 2, 3], backend = [1, 2, 1]
Output: 2 
Explanation:

The possible valid pairs which can be made are:
    
(frontend[1], backend[0])=(2, 1) and (frontend[2], backend[2])=(3, 1) are valid pairs.

(frontend[1], backend[0])=(2, 1) and (frontend[2], backend[1])=(3, 2) are valid pairs.

  
It can be seen that a maximum of 2 valid pairs can be made at a time. So the maximum number of pairs that can be formed is 2. Return 2.
  3-2-1
    i
  1 2 1
      i

'''
from typing import List

## INPUTS
frontend = [1, 2, 3]
backend = [1, 2, 1]

frontend = [4, 2, 1, 3]
backend = [1, 3, 2, 4]

frontend = [4, 5, 6]
backend = [2, 2, 2]

frontend = [3, 3, 3]
backend = []

def getMaxPairs(frontend:List[int], backend:List[int])-> int:
    pairs = 0

    frontend.sort(reverse=True)
    backend.sort(reverse=True)

    f, b = 0,0

    while f < len(frontend) and b < len(backend):
        if frontend[f] > backend[b]:
            pairs += 1
            f += 1
            b += 1
        else:
            b += 1

    return pairs

print(getMaxPairs(frontend,backend))