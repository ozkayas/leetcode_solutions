from heapq import heapify, heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapify(maxHeap)

        for x , y in points:
            dist = (x**2+y**2)
            heappush(maxHeap, (-dist, x, y))

            while len(maxHeap) > k:
                heappop(maxHeap)

        return [[x,y] for _,x,y in maxHeap]
        


        