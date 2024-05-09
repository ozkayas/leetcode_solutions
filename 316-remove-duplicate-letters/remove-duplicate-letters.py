class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastIndex = {ch:i for i, ch in enumerate(s)}
        #String builder
        stack = []

        for i, ch in enumerate(s):
            # We do not need an extra isSeen set or IndexSearcharray, 
            # in worst case we will 26 chars, so this loop up is OK
            if ch not in stack:
                # Remove all pushed chars that are greater than ch, and can be added later
                while stack and stack[-1] > ch and lastIndex[stack[-1]] > i:
                    stack.pop()
                
                stack.append(ch)


        return "".join(stack)
                