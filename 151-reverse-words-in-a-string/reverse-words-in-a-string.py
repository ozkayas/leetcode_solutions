class Solution:
    def reverseWords(self, s: str) -> str:

        strBuilder = deque()

        start = -1
        i = 0

        while i < len(s):
            if s[i] == " ":
                i += 1
            else:
                start = i
                while i < len(s) and s[i] != " ":
                    i += 1 
                sub = s[start:i]
                strBuilder.appendleft(sub)

        return " ".join(strBuilder)
        