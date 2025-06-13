class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        def dist(point:List[int]) -> float:
            return point[0]**2 + point[1]**2

        for p in points:
            heapq.heappush(maxHeap, (-dist(p), p))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        return [p for (_, p) in maxHeap]



