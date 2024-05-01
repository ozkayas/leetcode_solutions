import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)
        # 1 2 - 30 40 
        # maxH - minHeap
        

    def addNum(self, num: int) -> None:

        heapq.heappush(self.maxHeap, -num)
        heapq.heappush(self.minHeap, -self.maxHeap[0])
        heapq.heappop(self.maxHeap)

        # check lengths and balance, by pop and pushing
        while len(self.minHeap) > len(self.maxHeap):
            itemToMove = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -itemToMove)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + -self.maxHeap[0]) / 2
        else:
            return -self.maxHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()