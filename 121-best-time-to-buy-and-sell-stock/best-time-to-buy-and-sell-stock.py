class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = float('inf')
        profit = 0
        for p in prices:
            minSoFar = min(minSoFar, p)
            profit = max(profit, (p-minSoFar))

        return profit
        