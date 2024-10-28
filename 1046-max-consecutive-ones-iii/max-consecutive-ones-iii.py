class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l = r = 0
        zeros = 0
        maxLen = 0

        while r < N:
            if nums[r] == 0:
                zeros += 1
            if zeros <= k:
                maxLen = max(maxLen, r-l+1)
            
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            r += 1

        return maxLen

        