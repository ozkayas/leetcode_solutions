class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def fn(i):
            if i < 0: return 0
            if i not in memo:
                memo[i] =  max(nums[i]+fn(i-2), fn(i-1))
            return memo[i]
            


        return fn(len(nums)-1)     
