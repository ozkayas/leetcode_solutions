class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3: return max(nums)
        dp = [0 for _ in range(len(nums))]
        dp[0]= nums[0]
        dp[1]= nums[1]
        
        for i in range(2, len(nums)):
            prev = dp[i-1]-nums[i-1]
            prevprev = dp[i-2]
            dp[i] = max(prev,prevprev) + nums[i]
        
        return max(dp[-1],dp[-2])


"""
[2,7, 9, 1, 3,  1] 
 2 7  11  

 2 1 1 2
 2 1 
 """