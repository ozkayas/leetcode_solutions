class Solution:
    def reverseParentheses(self, s: str) -> str:

        stack = [""]
        for ch in s:
            if ch == "(":
                stack.append("")
            elif ch == ")":
                lastW = stack.pop()
                if stack:
                    stack[-1] += lastW[::-1]
                else:
                    return lastW[::-1]
            else:
                stack[-1] += ch
        
        return stack[-1]

'''
(ed(et(oc))el)
(ed(etco)el)
(edocteel)
leetcode

'''
        