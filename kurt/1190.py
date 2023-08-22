class Solution:
    def reverseParentheses(self, s: str) -> str:
        swp = ""
        lst = list(s)
        open_par = []

        for i in range(len(s)):
            if s[i] == '(':
                open_par.append(i)
            elif s[i] == ')':
                open_ind = open_par.pop()
                j = i
                while open_ind < j:
                    swp = lst[open_ind]
                    lst[open_ind] = lst[j]
                    lst[j] = swp
                    open_ind += 1
                    j -= 1

        ret = ''.join(lst).replace("(", "")
        ret = ret.replace(")", "")

        return ret