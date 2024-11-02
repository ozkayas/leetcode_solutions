class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        lead = 0

        # leader & follower pointers
        while lead < len(nums):
            for i in range(lead):
                if nums[i] < nums[lead]:
                    dp[lead] = max(dp[lead], dp[i] + 1)

            lead += 1

        return max(dp)


        