class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        maxHeap = []

        for a, b in classes:
            possibleGain = (a+1)/(b+1) - a/b
            heapq.heappush(maxHeap, (-possibleGain, a, b))

        while extraStudents:
            _, a, b = heapq.heappop(maxHeap)
            a += 1
            b += 1
            possibleGain = (a+1)/(b+1) - a/b
            heapq.heappush(maxHeap, (-possibleGain, a, b))

            extraStudents -= 1

        total = sum([a/b for _ ,a ,b in maxHeap])
        return total/len(classes)

        