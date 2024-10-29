class MedianFinder:

    def __init__(self):
        # 1 2 3 4 5 - 6 7 8 9 => try to hold median at maxHeap, if len odd
        # maxHeap - minHeap
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)
        rootMin = heapq.heappop(self.minHeap)
        heapq.heappush(self.maxHeap, -rootMin)
        self.balanceHeaps()

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        else:
            return -self.maxHeap[0]

    def balanceHeaps(self):
        if len(self.maxHeap) > len(self.minHeap)+1:
            maxVal = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, maxVal)