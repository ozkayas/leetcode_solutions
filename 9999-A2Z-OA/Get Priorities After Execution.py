"""
Java Medium Cozumu
https://medium.com/@milindaws3/solving-a-process-scheduling-puzzle-e1cc378f113c

Several processes are scheduled for execution on an AWS server.

On one server, n processes are schedule where the ith process is assigned a priority of priority[i]. The processes are placed sequentially in a queue and are numbered 1, 2,..,n. The server schedules the processes per the following algorithm:

1. It finds the maximum priority shared by at least 2 processes. Let that be denoted by p. (if there is no such priority or p = 0, the algorithm is terminated)
2. Otherwise, select the two of the processes with the lowest indexes and priority p, call them process1 and process2.
3. The server executes process1 and removes it from the queue.
4. To avoid starvation, it reduces the priority of process2 to floor(p/2).
5. Start again from step 1.
Given the initial priority of the processes, find the final priority of the processes which remain after the algorithm terminates.
Note that relative the arrangement of remaining processes in the queue remains the same,only their priorities change.
Function Description
Complete the function getPrioritiesAfterExecution in the editor.
getPrioritiesAfterExecution has the following parameter:
int priority[n]: the initial prorities of processes
Returns

int[]: the final priorities of the remaining processes
Example 1:
Input:  priority = [6, 6, 6, 1, 2, 2]
Output: [3, 6, 0]
Explanation:
The scheduler works as follows:
1. p = 6 at indices 1, 2 and 3. The indices used are process1 = 1, process2 = 2. Remove process 1 and update the priority of process 2 to floor(6/2) = 3.
2. p = 2 and process1 = 4, process2 = 5. So, update the priority = floor(2/2) = 1 of process2 and remove process1. Current set of process priorities, priority = [3, 6, 1, 1].
3. p = 1 and process 1 = 3, process2 = 4. So, update the priority = floor(1/2) = 0 of process2 and remove process1. Current set of process priorities, priority = [3, 6, 0].
4. There are no more matching process priorities so the algorithm ends.

The final priorities of the reamining processes are priority = [3, 6, 0].
Example 2:
Input:  priority = [4, 4, 2, 1]
Output: [0]
Explanation:
p = 4 and process1 = 1, process2 = 2. So, update the priority = floor(4/2) = 2 of process2 and remove process1. Current set of process priorities, priority = [2, 1, 1].
p = 2 and process1 = 1, process2 = 2. So, update the priority = floor(2/2) = 1 of process2 and remove process1. Current set of process priorities, priority = [1, 1].
p = 1 and process1 = 1, process2 = 2. So, update the priority = floor(1/2) = 0 of process2 and remove process1. Current set of process priorities, priority = [0].
Example 3:
Input:  priority = [2, 1, 5, 10, 10, 1]
Output: [0, 1]
Explanation:
p = 10 and process1 = 4, process2 = 5. So, update the priority = floor(10/2) = 5 of process2 and remove process1. Current set of process priorities, priority = [2, 1, 5, 5, 17].
p = 5 and process1 = 3, process2 = 4. So, update the priority = floor(5/2) = 2 of process2 and remove process1. Current set of process priorities, priority = [2, 1, 2, 17].
p = 2 and process1 = 1, process2 = 3. So, update the priority = floor(2/2) = 1 of process2 and remove process1. Current set of process priorities, priority = [1, 1, 17].
p = 1 and process1 = 1, process2 = 2. So, update the priority = floor(1/2) = 0 of process2 and remove process1. Current set of process priorities, priority = [0, 1].
"""
import heapq
from typing import List


def getPrioritiesAfterExecution(priority: List[int]) -> List[int]:
    maxHeap = []
    for i, p in enumerate(priority):
        maxHeap.append((-p,i))
    heapq.heapify(maxHeap)

    temp = []
    while maxHeap:
        cur, i = heapq.heappop(maxHeap)
        if not temp:
            temp.append((cur,i))
        elif temp[-1][0] != cur:
            temp.append((cur,i))
        else:
            #we found a pair, pop last element in temp, update cur and add
            temp.pop()
            # half the cur val, -3//2 = -2 but 3//2 = 1 !!!!!
            cur = -cur//2
            temp.append((-cur, i))

            # addd temp back into heap
            while temp:
                heapq.heappush(maxHeap, temp.pop())
    # print(maxHeap)
    ans = []
    temp.sort(key= lambda pair:pair[1])
    return [-pair[0] for pair in temp]

print(getPrioritiesAfterExecution([6,6,6,1,2,2])) ### 3,6,0
print(getPrioritiesAfterExecution([4, 4, 2, 1])) ### 0
print(getPrioritiesAfterExecution([2, 1, 5, 10, 10, 1])) ### 0 1
