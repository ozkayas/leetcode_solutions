class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float("inf") for _ in range(amount+1)]
        dp[0] = 0
        N = len(dp)

        for i in range(N):
            for coin in coins:
                if i+coin < N:
                    dp[i+coin] = min(dp[i+coin], dp[i]+1)


        return -1 if dp[amount] == float("inf") else dp[amount]
        