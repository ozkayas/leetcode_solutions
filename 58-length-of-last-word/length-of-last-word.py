class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p = len(s)-1
        e = 0

        while s[p].isspace():
            p -= 1
        
        e = p

        while p > 0 and s[p-1].isalpha():
            p -= 1
        
        return e - p + 1


        