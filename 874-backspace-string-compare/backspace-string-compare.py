class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        nonMatchingIndex = -1
        sLast, pLast = "", ""
        sp, tp = len(s)-1, len(t)-1 

        # Return the last valid character
        def getLastValidCharIndex(s:str, i:int) -> int:
            count = 0
            while i >= 0:
                if s[i] == "#":
                    count -=1
                else:
                    count += 1
                if count > 0:
                    return i 
                i -= 1
            return i

        # print(getLastValidCharIndex(s, sp))

        sp = getLastValidCharIndex(s,sp)
        tp = getLastValidCharIndex(t,tp)
        while sp > -1 and tp > -1 and s[sp] == t[tp]:
            sp = getLastValidCharIndex(s, sp-1)
            tp = getLastValidCharIndex(t, tp-1)
                
        if sp == -1 and tp == -1:
            return True
        else:
            return False