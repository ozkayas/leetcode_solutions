class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums] 
        heapq.heapify(nums)
        score = 0

        for _ in range(k):
            cur = -heapq.heappop(nums) 
            score += cur

            new = math.ceil(cur/3)
            heapq.heappush(nums, -new)
        
        return score
        