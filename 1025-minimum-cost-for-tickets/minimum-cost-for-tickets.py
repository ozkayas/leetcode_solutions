class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        lastDay = days[-1]
        # dp[day] Holds cost for the day
        dp = [0 for _ in range(lastDay+1)]

        i = 0 # to keep track which day we are checking
        for d in range(1, lastDay+1):
            if d < days[i]: # say we are checking 1.st day but days = [3,4,...], then skip until d == 3
                dp[d] = dp[d-1]
            else:
                i += 1
                dp[d] = min({dp[d - 1] + costs[0],
                               dp[max(0, d - 7)] + costs[1],
                               dp[max(0, d - 30)] + costs[2]})


        return dp[lastDay]