class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        dp = [0 for _ in range(n)]

        dp[-1], dp[-2] = cost[-1], cost[-2]

        print(dp)
        for i in range(n-2-1,-1,-1):
            print(i)
            dp[i] = cost[i] + min(dp[i+1],dp[i+2])


        return min(dp[0], dp[1])

