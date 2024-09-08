class Solution:
    def isValid(self, s: str) -> bool:
        open = {")":"(", "]":"[", "}":"{"}
        stack = []

        for ch in s:
            if not stack or ch not in open.keys():
                stack.append(ch)
            else:
                if stack[-1] == open[ch]:
                    stack.pop()
                else:
                    return False
        
        return False if stack else True

        