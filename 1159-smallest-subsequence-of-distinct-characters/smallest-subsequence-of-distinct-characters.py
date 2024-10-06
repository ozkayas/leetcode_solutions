class Solution:
    def smallestSubsequence(self, s: str) -> str:
        lastIndex = {ch:i for i,ch in enumerate(s)}
        stack = []

        for i, ch in enumerate(s):
            if ch in stack:
                continue
            while stack and stack[-1] > ch and lastIndex[stack[-1]] > i:
                stack.pop()
            
            stack.append(ch)

        return "".join(stack)
        