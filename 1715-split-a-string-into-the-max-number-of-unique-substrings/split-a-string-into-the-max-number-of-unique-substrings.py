class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        mx = 0
        def backtrack(sub:set, s:str):
            nonlocal mx
            if s == "":
                mx = max(mx, len(sub))
            for i in range(len(s)):
                if s[0:i+1] not in sub:
                    sub.add(s[0:i+1])
                    backtrack(sub, s[i+1:])
                    sub.remove(s[0:i+1])

        backtrack(set(), s)

        return mx


"""
"addbsd"

"""