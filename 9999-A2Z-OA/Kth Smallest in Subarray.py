'''
Kth Smallest in Subarray 🍒
Given an array arr, return the kth smallest integer for each subarray of size m.

Example 1:

Input:  arr = [3, 1, 4, 2], k = 2, m = 3
Output: [3, 2] 
Explanation:

In the first subarray of size 3 ([3,1,4]) the 2nd smallest element is 3. In the second subarray of size 3 ([1,4,2]) the 2nd smallest element is 2.
'''
from typing import List
import heapq
from sortedcontainers import SortedList

def giveSmallestNums(arr:List[int], k:int, m:int)->List[int]:
    res = []
    #Use a maxheap of len k- for each step push and pop to this heap
    #Create maxheap and fill the base cases
    maxHeap = [i * -1 for i in arr[0:m]]  ## Negating for maxHeap
    heapq.heapify(maxHeap)
    nLargest = heapq.nlargest(k, maxHeap)
    res.append(nLargest[-1]*-1)

    N = len(arr)
    i = m

    while i < N:
        ## update sub array bu removing and adding to the heap
        toRemove = arr[i-m]
        toAdd = arr[i]
        # print("r,a",toRemove, toAdd)
        # heapq does not have a remove method, so remove it from the list and then heapify again
        for n in maxHeap:
            if n == toRemove * -1:
                maxHeap.remove(n)
        heapq.heapify(maxHeap)
        heapq.heappush(maxHeap,toAdd * -1)
        nLargest = heapq.nlargest(k, maxHeap)
        res.append(nLargest[-1]*-1)
        i += 1

    return res

### Same implementation but using sortedList instead of heap
def giveSmallestWithSortedList(arr:List[int], k:int, m:int)->List[int]:
    res = []
    sl = SortedList()

    # Fill base case in SL
    for n in arr[:m]:
        sl.add(n)

    # add kth of base case
    res.append(sl[k-1])

    N = len(arr)
    i = m

    while i < N:
        ## update sub array bu removing and adding to the sorted List
        toRemove = arr[i-m]
        toAdd = arr[i]
        sl.discard(toRemove)
        sl.add(toAdd)
        res.append(sl[k-1])
        i += 1

    return res


# arr, k, m = [3, 1, 4, 2], 2, 3
arr, k, m = [3, 1, 4, 2, 2], 2, 3
# arr, k, m = [3, 1, 4, 2, 5, 5, 1], 2, 3

print(giveSmallestNums(arr,k,m))
print(giveSmallestWithSortedList(arr,k,m))
