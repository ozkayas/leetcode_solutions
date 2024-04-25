class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        if len(s) == 1: return 1

        ## Implementing the top-down Editorial solution
        ## Time: O(26 * len(s)) - Space: O(26 * len(s))
        dp = [[0 for _ in range(26)] for _ in range(len(s))]

        for i, ch in enumerate(s):
            # fill the first row for first letter as the base case
            chNum = ord(ch)-ord("a")
            if i == 0:
                dp[i][chNum] = 1
            
            # Using min, max to stay in bounds
            # Search for candidates of previous row, that we can attach this ch
            dp[i] = dp[i-1].copy()
            start = max(0, chNum - k)
            end = min(25, chNum + k)

            max_prev = max(dp[i-1][start:end+1])
            dp[i][chNum] = max_prev +1

        # print(dp)
        return max(dp[-1])
