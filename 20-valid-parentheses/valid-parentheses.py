class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')':'(', '}':'{', ']':'['}

        stack  = []
        for ch in s:
            if ch in closeToOpen.values():
                stack.append(ch)
            elif stack and stack[-1] == closeToOpen[ch]:
                stack.pop()
            else:
                return False
        
        return False if stack else True
             
        