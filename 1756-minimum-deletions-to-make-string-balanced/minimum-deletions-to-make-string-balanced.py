class Solution:
    def minimumDeletions(self, s: str) -> int:
        bPref, aSuf = [], []
        
        cnt = 0
        for ch in s:
            bPref.append(cnt)
            if ch == "b": cnt += 1
        cnt = 0
        for ch in s[::-1]:
            aSuf.append(cnt)
            if ch == "a": cnt += 1
        aSuf.reverse()
        
        ans = len(s)
        for i in range(len(s)):
            ans = min(ans, bPref[i]+aSuf[i])
        
        return ans

'''
Approach 1: prefix loop then update variable. 
N = 8
 0 0 0 1 1 2 3 3   - b prefix
"a a b a b b a b"
 3 2 2 1 1 1 0 0




'''