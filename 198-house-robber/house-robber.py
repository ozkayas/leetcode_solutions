class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 3: return max(nums)
        dp = [0 for _ in range(N)]
        dp[0], dp[1] = nums[0], nums[1]


        for i in range(2, N):
            pre = dp[i-1] - nums[i-1]
            prePre = dp[i-2]
            dp[i] = max(pre, prePre) +nums[i]

        return max(dp)