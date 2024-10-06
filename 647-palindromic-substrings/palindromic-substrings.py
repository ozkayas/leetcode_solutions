class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        ans = 0
        #DP solution
        dp = [[False for _ in range(N)] for _ in range(N)]

        for i in reversed(range(N)):
            dp[i][i] = True
            ans += 1
            for j in range(i+1,N):
                if s[i] == s[j]: 
                    if j - i == 1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        ans += 1

        return ans


        