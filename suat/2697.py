class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l = list(s)
        p1, p2 = 0, len(s)-1

        while p1 < p2:
            if ord(l[p1]) < ord(l[p2]):
                l[p2] = l[p1]
            elif ord(l[p1]) > ord(l[p2]):
                l[p1] = l[p2]
            p1 += 1
            p2 -= 1    
        
        return ''.join(l)