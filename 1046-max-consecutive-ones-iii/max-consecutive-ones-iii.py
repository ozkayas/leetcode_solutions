class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zeroCount = 0
        maxLen = 0

        for r in range(len(nums)):

            if nums[r] == 0:
                zeroCount += 1
            
            while zeroCount > k:
                charAtHead = nums[l]
                if charAtHead == 0:
                    zeroCount -= 1
                l += 1

            maxLen = max(maxLen, (r-l+1))


        return maxLen


