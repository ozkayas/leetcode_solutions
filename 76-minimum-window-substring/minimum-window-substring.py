class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        output, res = float("inf"), ""
        lookup = Counter(t)
        count = len(lookup) # count == 0 means window contains t
        st, end = 0, 0

        while end < len(s):
            # Move end pointer until windown contains t
            while end < len(s) and count != 0:
                cur = s[end]
                if cur in lookup:
                    lookup[cur] -= 1
                    if lookup[cur] == 0:
                        count -= 1
                end += 1

            # Move start pointer until window doesnt cointain t
            while st < end and count == 0:
                if end-st < output:
                    output = end-st
                    res = s[st:end]

                cur = s[st]
                if cur in lookup:
                    lookup[cur] += 1
                    if lookup[cur] > 0:
                        count += 1
                
                st += 1
            
        return res
                

