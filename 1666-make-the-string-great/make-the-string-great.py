class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        ans = ""

        for char in s:
            if not stack:
                stack.append(char)
                
            else:
                if stack[-1] != char and stack[-1].lower() == char.lower():
                    stack.pop()
                else:
                    stack.append(char)
        
        return "".join(stack)