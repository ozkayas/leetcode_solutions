class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # Update heap with lazy removal and return the top of the heap
        def currentMax(maxHeap, removed) -> int:
            while maxHeap and maxHeap[0][1] in removed:
                val, indx = heapq.heappop(maxHeap)
                removed.discard(indx)
            return maxHeap[0][0]


        # Lets hold the indexes of removed from heap, lazy removal
        removed = set()
        # init heap, will hold tuples value & index => {(1,0),(3,1),(-1,2)}
        maxHeap = []
        for i in range(k):
            maxHeap.append((-nums[i], i))
        heapq.heapify(maxHeap)
        ans = []
        ans.append(-maxHeap[0][0])



        # Shift window and update heap, then write the max
        l, r = 0, k-1
        while r < len(nums)-1:
            removed.add(l)

            heapq.heappush(maxHeap, (-nums[r+1], r+1))

            maxInWindow = currentMax(maxHeap, removed)
            ans.append(-maxInWindow)
            l += 1
            r += 1
        return ans



        
        