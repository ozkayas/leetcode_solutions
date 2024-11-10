class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opens, closes = 0, 0
        stack = []

        # First pass: add all "(", do not add ")" if has no match.
        for ch in s:
            if ch == "(":
                opens += 1
                stack.append(ch)
            elif ch == ")":
                if opens > closes: # We can add closing
                    closes += 1
                    stack.append(ch)
            else:
                stack.append(ch)
        
        if opens == closes:
            return "".join(stack)

        # Now strBuilder may have excessive openings.
        # We reverse iterate with the current states of opens & closes and process
        strBuilder = []
        for ch in reversed(stack):
            if ch == "(" and opens > closes:
                opens -= 1
                continue
            else:
                strBuilder.append(ch)

        return "".join(reversed(strBuilder))



        