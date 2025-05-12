class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1 for _ in range(N)]

        leader = 0
        while leader < N:
            for i in range(leader):
                if nums[i] < nums[leader]:
                    dp[leader] = max(dp[leader], dp[i]+1)
            leader += 1

        return max(dp)



        