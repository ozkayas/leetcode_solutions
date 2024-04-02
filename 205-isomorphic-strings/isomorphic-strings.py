class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = dict()

        for i in range(len(s)):
            ch = s[i]
            if ch not in m:
                if t[i] in m.values():
                    return False
                m[ch] = t[i]
            else:
                if m[ch] != t[i]:
                    return False

        return True
        