class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0

        for i in range(len(dp)):
            for c in coins:
                if i+c <= amount:
                    dp[i+c] = min(dp[i+c], dp[i]+1)

        return -1 if dp[-1] == float("inf") else dp[-1]


