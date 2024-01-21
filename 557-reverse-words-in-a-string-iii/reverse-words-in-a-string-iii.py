class Solution:
    def reverseWords(self, s: str) -> str:
        h, t = 0,0
        resList = []

        while t < len(s):
            if s[t] == " " or t == len(s)-1:
                word = s[h:t] if s[t] == " " else s[h:t+1]
                # print(word)
                resList.append(word[::-1])
                # res += word[::-1]+" " if s[t] == " " else word[::-1]
                h = t+1
            
            t += 1

        return " ".join(resList)
 