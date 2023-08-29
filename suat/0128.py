class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxSubLen = 0
        
        # we try to find if num can be the first item of a sequence
        for num in nums:
            if num-1 not in numsSet: # this num can be the first 
                i = num             # i first item of candidate sequence
                while i in numsSet:
                    i += 1
                maxSubLen = max(maxSubLen, i  - num)
        
        return maxSubLen