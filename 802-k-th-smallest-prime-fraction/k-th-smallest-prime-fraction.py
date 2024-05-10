class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        minHeap = []
        heapq.heapify(minHeap)
        N = len(arr)
        
        # Populate min heap with fractions
        for i in range(N):
            for j in range(i + 1, N):
                fraction = (arr[i] / arr[j], (arr[i], arr[j]))
                heapq.heappush(minHeap, fraction)
        
        # Pop k-1 smallest fractions
        for _ in range(k - 1):
            heapq.heappop(minHeap)
        
        # Return the k-th smallest fraction
        return heapq.heappop(minHeap)[1]