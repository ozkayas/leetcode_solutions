class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opens = closes = 0

        for ch in s:
            if ch == "(":
                opens += 1
            else:
                if opens > 0:
                    opens -= 1
                else:
                    closes += 1

        return opens + closes
        