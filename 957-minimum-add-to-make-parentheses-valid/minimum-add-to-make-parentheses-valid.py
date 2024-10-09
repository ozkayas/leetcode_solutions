class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        o, c = 0, 0
        for ch in s:
            if ch == "(":
                o += 1
            else:
                if o > 0: 
                    o -= 1
                else:
                    c += 1
        return o + c
        