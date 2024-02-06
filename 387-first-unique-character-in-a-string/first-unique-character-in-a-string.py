class Solution:
    def firstUniqChar(self, s: str) -> int:
        ctr = Counter(s)
        
        for i in range(len(s)):
            if ctr[s[i]] == 1:
                return i
        
        return -1
        