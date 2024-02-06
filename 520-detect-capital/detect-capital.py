class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # A : 65 Z: 90 a: 97 z: 122
        capitals = 0
        isFirstCapital = 65<=ord(word[0])<=90

        for i in range(len(word)):
            if 65<=ord(word[i])<=90:
                capitals += 1
        
        if capitals == len(word):
            return True
        if isFirstCapital and capitals == 1:
            return True
        if capitals ==  0:
                return True 
        
        return False 

        