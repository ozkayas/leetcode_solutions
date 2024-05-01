class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        output = ''
        
        for i in range(len(word)):
            if word[i] == ch:
                output += word[i::-1]
                output += word[i+1:]
                return output
        
        return word

         