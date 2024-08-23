class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        counter = 0
        while nums and nums[0] < k:
            heapq.heappop(nums)
            counter += 1
        
        return counter