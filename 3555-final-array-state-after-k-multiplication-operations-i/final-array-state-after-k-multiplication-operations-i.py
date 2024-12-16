class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        minHeap = []
        for i, n in enumerate(nums):
            minHeap.append((n, i))
        heapq.heapify(minHeap)

        for _ in range(k):
            val, i = heapq.heappop(minHeap)
            nums[i] = val * multiplier
            heapq.heappush(minHeap, (val * multiplier, i))

        return nums

        