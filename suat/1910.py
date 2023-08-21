class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = ""
        n = len(part)
        for ch in s: 
            stack += ch
            if stack[-n:] == part: 
                stack = stack [:-n]
        return stack