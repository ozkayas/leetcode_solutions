class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        def isPalindrome(s):
            p1, p2 = 0, len(s)-1

            while p1 <= p2:
                if s[p1] != s[p2]:
                    return False
                p1+=1
                p2-=1    
            return True
        
        for word in words:
            if isPalindrome(word): return word

        return ''
        