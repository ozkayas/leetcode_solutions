class Solution:
    def halvesAreAlike(self, s: str) -> bool:
       l, r = 0, len(s)-1 
       counter = 0
       vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}


    
       while l<r:
            if s[l] in vowels:
                counter += 1
            if s[r] in vowels:
                counter -= 1

            l += 1
            r -= 1

       return counter == 0
