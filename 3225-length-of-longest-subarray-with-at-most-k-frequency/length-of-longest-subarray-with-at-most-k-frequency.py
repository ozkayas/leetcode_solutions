class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l,r = 0,0
        m = dict()
        ans = 0

        while r < N:
            rNum = nums[r]
            m[rNum] = 1 + m.get(nums[r], 0)
            if m[rNum] <= k:
                ans = max(ans, (r-l+1))
            else:
                while m[rNum] > k:
                    m[nums[l]] -= 1
                    l += 1


            r += 1 
        
        return ans