class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[amount] will hold state , how many min coins needed to reach this sate
        # dp[11] = 3, dp[0] = 0
        # Forward push dp

        dp = [float('inf') for i in range(amount+1)]
        dp[0] = 0

        # try to fill each dp state
        N = len(dp)
        for i in range(N):
            # try to jump to next possible states from this state
            for coin in coins:
                if (i + coin) < N:
                    dp[i + coin] = min(dp[i+coin] , (dp[i] + 1))

        return dp[amount] if dp[amount] < float("inf") else -1
'''
            i
0 1 2 3 4 5 6 7 8 9 10 11
0 1 1 2 2 1 2 2 3 3 2  3
'''