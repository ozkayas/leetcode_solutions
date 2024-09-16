from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        m = {"I":1, "V":5, "X": 10, "L":50, "C":100, "D":500, "M":1000}

        i = val = 0
        while i < len(s)-1:
            this = m[s[i]]
            nxt = m[s[i+1]]
             
            if this >= nxt:
                val += this
                i += 1
            else: # IV 5-1
                val += (nxt - this)
                i += 2

        if i == len(s)-1:
            val += m[s[i]]

        return val
            
        


