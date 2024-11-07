class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        R, C = len(word2), len(word1)
        # https://www.youtube.com/watch?v=HwDXH35lr0o&ab_channel=NikhilLohia
        dp = [[0 for _ in range(C+1)] for _ in range(R+1)] # word 1 on top horizontal, word 2 vertical

        # İlk satır ve sütunu başlatıyoruz
        for r in range(1, R+1):
            dp[r][0] = r
        for c in range(1, C+1):
            dp[0][c] = c

        ## Attention dp[1] = word[0] -> index farkina dikkat ederek yaz
        for r in range(1,R+1):
            for c in range(1, C+1):
                if word1[c-1] == word2[r-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = 1+ min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])

        return dp[-1][-1]



