class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        maxHeap = []
        for a, b in classes:
            # possible upgrade gain of this class
            upgrade = (a+1)/(b+1) - (a/b)
            maxHeap.append((-upgrade, a, b))

        heapq.heapify(maxHeap)

        while extraStudents:
            # pop the class with max possible gain and add +1 student to it
            _, a, b = heapq.heappop(maxHeap)
            a+=1
            b+=1
            upgrade = (a+1)/(b+1) - a/b
            heapq.heappush(maxHeap,(-upgrade, a, b))

            extraStudents -= 1
        
        total = sum([a/b for _,a,b in maxHeap])
        
        return total/len(maxHeap)
        