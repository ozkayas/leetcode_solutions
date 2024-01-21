class Solution:
    def reverseWords(self, s: str) -> str:
        h, t = 0,0
        res = ""

        while t < len(s):
            if s[t] == " " or t == len(s)-1:
                word = s[h:t] if s[t] == " " else s[h:t+1]
                # print(word)
                res += word[::-1]+" " if s[t] == " " else word[::-1]
                h = t+1
            
            t += 1

        return res
 