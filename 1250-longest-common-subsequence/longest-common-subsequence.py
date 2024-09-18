class Solution:
    # https://excalidraw.com/#json=Ow9nYUQyijXGEZLDtR84b,q9LA6r_1zQLUJPc9Eh3A0Q
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        R = len(text1)
        C = len(text2)

        # dp matrisini bir satır ve bir sütun fazlasıyla başlatıyoruz (0. indeks için boşluk)
        dp = [[0] * (C + 1) for _ in range(R + 1)]
        ans = 0

        # Fill this cell and return the filled value also
        def fillCell(r, c) -> int:
            if text1[r-1] == text2[c-1]:  # 0 indeksli dizilerdeki karakterleri karşılaştır
                dp[r][c] = dp[r-1][c-1] + 1
            else:
                dp[r][c] = max(dp[r-1][c], dp[r][c-1])
            return dp[r][c]

        for r in range(1, R + 1):
            for c in range(1, C + 1):
                n = fillCell(r,c)
                ans = max(n, ans)

        return ans

"""
    a c e
a.  1 1
b
c
d
e

"""
                    

        