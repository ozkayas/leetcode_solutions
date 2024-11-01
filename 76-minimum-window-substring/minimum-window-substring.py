class Solution:
    def minWindow(self, s:str, t: str) -> str:
        freqT = Counter(t) # Indicator if we depleted all 
        l, r = 0, 0
        completedCharCounter = 0 # should reach len(freqT) ,for the validity of the window
        res = None

        def updateRes(l,r):
            nonlocal res
            if res == None or (r-l+1) < len(res):
                res = s[l:r+1]

        while r < len(s):
            ch = s[r]
            # We process if we are interested in this char: it is also in t
            if ch in freqT:
                freqT[ch] -= 1
                if freqT[ch] == 0: 
                    completedCharCounter += 1
            
            # Shrink window until window is not valid
            while completedCharCounter == len(freqT):
                # Save this substring as a potential result
                updateRes(l, r)

                leftMostCh = s[l]
                if leftMostCh in freqT:
                    freqT[leftMostCh] += 1
                    if freqT[leftMostCh] > 0:
                        completedCharCounter -= 1

                l += 1 

            r += 1
        return res if res else ""

        