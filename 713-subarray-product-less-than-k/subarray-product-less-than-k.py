class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        
        l,r = 0,0
        prod = 1
        ans = 0

        while r < len(nums):
            prod *= nums[r]
            while prod >= k:
                prod /= nums[l]
                l += 1
            
            if prod < k:
                ans += (r-l+1)

            r += 1
        
        return ans



        