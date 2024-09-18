class Solution:
    # https://excalidraw.com/#json=Ow9nYUQyijXGEZLDtR84b,q9LA6r_1zQLUJPc9Eh3A0Q
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        R = len(text1)
        C = len(text2)

        dp = [[0 for _ in range(C)] for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if r == 0 and c == 0:
                    if text1[r] == text2[c]:
                        dp[r][c] = 1
                elif r == 0:
                    if text1[r] == text2[c]:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = dp[r][c-1]
                elif c == 0:
                    if text1[r] == text2[c]:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = dp[r-1][c]

                else:
                    if text1[r] == text2[c]:
                        dp[r][c] = dp[r-1][c-1] + 1
                    else:
                        dp[r][c] = max(dp[r-1][c], dp[r][c-1])

        ans = 0
        for row in dp:
            for n in row:
                ans = max(ans, n)

        return ans

"""
    a c e
a.  1 1
b
c
d
e

"""
                    

        