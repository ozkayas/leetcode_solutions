class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        r = s[::-1]
        N = len(s)
        # Find longest common subsequence s and r
    
        dp = [[0 for _ in range(N)] for _ in range(N)]
    
        for i in range(N):
            for j in range(N):
                if r[i] == s[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] +1
                else:
                    leftCell = dp[i][j-1]
                    upCell = dp[i-1][j]
                    dp[i][j] = max(leftCell, upCell)
    
        return dp[-1][-1]

    def minInsertions(self, s: str) -> int:
        longestPalindrome = self.longestPalindromeSubseq(s)

        return len(s) - longestPalindrome
        