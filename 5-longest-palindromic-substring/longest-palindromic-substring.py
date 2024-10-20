class Solution:
    # search to both sides from the input index and returns the found palindrome
    def search(self,i:int, s:str) -> str:
        possiblePalindrome = ''
        # search for 1 letter in the center and to both sides "aaxaa" 
        #                                                        ^
        l, r = i, i
        while l-1 >= 0 and r+1 < len(s) and s[l-1] == s[r+1]:
                l -= 1
                r += 1
        
        possiblePalindrome = s[l:r+1]

        #search for 2 twin letters in the center, ie: "aaxxaa"
        #                                                ^
        if i+1 < len(s) and s[i] == s[i+1]:
            l, r = i, i+1
            while l-1 >= 0 and r+1 < len(s) and s[l-1] == s[r+1]:
                    l -= 1
                    r += 1

            # we found a longer candidate
            if len(s[l:r+1]) > len(possiblePalindrome):
                possiblePalindrome = s[l:r+1]

        return possiblePalindrome



    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            pal = self.search(i,s)
            if len(pal) > len(ans):
                ans = pal

        return ans

    
        