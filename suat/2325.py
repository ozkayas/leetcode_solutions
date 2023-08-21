class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        m = {}
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


        for c in key:
            if c not in m and c.isalpha():
                m[c] = alphabet[0]
                alphabet = alphabet[1:]

        
        result = ""
        for c in message:
            if c.isalpha():
                result += m[c]
            else: 
                result += c
        
        return result