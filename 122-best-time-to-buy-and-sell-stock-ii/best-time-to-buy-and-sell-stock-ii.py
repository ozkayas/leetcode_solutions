class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices)-1):
            curP = prices[i+1] - prices[i]
            if curP > 0:
                profit += curP


        return profit