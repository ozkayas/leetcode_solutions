class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = [-g for g in gifts]
        heapq.heapify(maxHeap)

        for _ in range(k):
            if maxHeap[0] == -1:
                return -sum(maxHeap)
            mx = -heapq.heappop(maxHeap)
            mx = math.floor(mx**0.5)
            heapq.heappush(maxHeap, -mx)

        return -sum(maxHeap)


        

        