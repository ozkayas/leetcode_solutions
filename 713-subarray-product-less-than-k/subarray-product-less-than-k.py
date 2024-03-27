class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1: return 0

        l, r, ans, prod = 0, 0, 0, 1

        while r < len(nums):
            prod *= nums[r]

            while prod >=k:
                prod /= nums[l]
                l += 1
            
            if prod < k:
                ans += (r-l+1)

            r += 1
        
        return ans