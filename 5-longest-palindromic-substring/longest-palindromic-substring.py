class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        longest = ""

        def pal(i, j)->str:
            if s[i] != s[j]: return ""
            while (i-1) >=0 and (j+1) < len(s) and s[i-1] == s[j+1]:
                i -= 1
                j += 1

            # print('found palindrome:', s[i:j+1])
            return s[i:j+1]

        # test = pal(2,2)
        # print(test)
        for i in range(0,len(s)-1,1):
            pal1 = pal(i,i)
            pal2 = pal(i, i+1)
            longest = max((longest,pal1,pal2), key= len)

        return longest


        