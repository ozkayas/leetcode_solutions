'''
https://www.fastprep.io/problems/amazon-find-requests-in-queue
Amazon Web Services (AWS) is a cloud computing platform with multiple servers. One of the servers is assigned to serve customer requests. There are n customer requests placed sequentially in a queue, where the ith request has a maximum waiting time denoted by wait[i]. That is, if the ith request is not served within wait[i] seconds, then the request expires and it is removed from the queue. The server processes the request following the First In First Out (FIFO) principle. The 1st request is processed first, and the nth request is served last. At each second, the first request in the queue is processed. At the next second, the processed request and any expired requests are removed from the queue.

Given the maximum waiting time of each request denoted by the array wait, find the number of requests present in the queue at every second until it is empty.

Note:

If a request is served at some time instant t, it will be counted for that instant and is removed at the next instant.
The first request is processed at time = 0. A request expires without being processed when time = wait[i]. It must be processed while time < wait[i].
The initial queue represents all requests at time = 0 in the order they must be processed.
Function Description

Complete the function findRequestsInQueue in the editor.

findRequestsInQueue has the following parameter:

int wait[n]: the maximum waiting time of each request

Input:  wait = [2, 2, 3, 1]
Output: [4, 2, 1, 0]

Input:  wait = [4, 4, 4]
Output: [3, 2, 1, 0] 

Input:  wait = [3, 1, 2, 1]
Output: [4, 1, 0] 
'''
import heapq
from typing import List



## My first code:
# def findRequestsInQueue(wait: List[int]) -> List[int]:
    
#     total_jobs = len(wait)
    
#     ans = [total_jobs] #Starting ans with current length

#     expired_jobs = set() ##To hold indexes of expireds
#     removed_jobs = 0 ## Just a counter for Processed and expired in total

#     ## Fill minheap
#     minHeap = []
#     for idx, wait_time in enumerate(wait):
#         heapq.heappush(minHeap, (wait_time, idx))
    

#     curr_time = 1
#     idx = 0
#     while removed_jobs < total_jobs:
#         # If faced an expired during iteraion on wait, just pass it
#         if idx in expired_jobs:
#             idx += 1
#             continue
        
#         # Process and remove
#         removed_jobs += 1
        
#         # Expire tasks <= curTime
#         while minHeap and minHeap[0][0] <= curr_time:
#             expired_time, expired_idx = heapq.heappop(minHeap)
#             if expired_idx > idx:
#                 expired_jobs.add(expired_idx)
#                 removed_jobs += 1
        
#         #print(minHeap, idx, removed_jobs)
#         ans.append(total_jobs - removed_jobs)
#         idx += 1
#         curr_time += 1
    
#     print(wait, ans)
#     return ans

## Second Trial




def findRequestsInQueue(wait:List[int]) -> List[int]: 
    minHeap = []
    heapq.heapify(minHeap)   ## Will hold tuples (value, index) to check versus lazy removed set
    ans = [len(wait)]
    lazy_removed = set() ## Will hold removed indexes lazily
    removedCount = 0
    
    #Fill heap:
    for i, jobTime in enumerate(wait):
        heapq.heappush(minHeap, (jobTime, i))

    for i in range(len(wait)):

        # STEP 1: lazy remove the first job
        if i in lazy_removed: # This may be expired long time ago, then just continue this index
            continue
        lazy_removed.add(i)
        removedCount += 1

        # STEP 2: remove all expired jobs:   
        # at t = 1 we are at index = 0 , so remove <=t values from heap & from removed if any
        while removedCount < len(wait) and minHeap[0][0] <= (i+1):
            t,index = heapq.heappop(minHeap)
            if index not in lazy_removed:
                lazy_removed.add(index)
                removedCount += 1
            

        # STEP 3: calculate remainings
        remaining_jobs = len(wait)-removedCount
        ans.append(remaining_jobs)
        if ans[-1] == 0:
            return ans

print(findRequestsInQueue([2, 2, 3, 1]))
print(findRequestsInQueue([4, 4, 4]))
print(findRequestsInQueue([3, 1, 2, 1]))