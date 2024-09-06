class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isValid(s: str) -> bool:
            N = len(s)
            if N == 0: return False
            elif N == 1: return True
            elif N == 2 and int(s) < 10: return False 
            elif N == 3 and int(s) < 100: return False 
            elif N == 3 and int(s) > 255: return False 
            elif N > 3: return False
            else: return True

        if len(s) < 4:
            return []
        # Whenever any dp finds a solution, will add it into this array
        ans = []

        # current string to be sliced and index of slot to fill in range(0,3)
        def dp(s:str, cur: List, i:int):
            
            # check if we have enough slots to slice 
            freeSlots = 4 - i
            if len(s) > freeSlots * 3: return

            # if filling the last slot/index fill it and add to the answer
            if i == 3:
                if isValid(s): 
                    cur[i] = s
                    ans.append(cur)
                return
            
            # Fill this slot with 1,2 or 3 characters
            if isValid(s[0:1]):
                cp1 = cur.copy() 
                cp1[i] = s[0:1]
                dp(s[1:], cp1, i+1)
            if isValid(s[0:2]):
                cp2 = cur.copy() 
                cp2[i] = s[0:2]
                dp(s[2:], cp2, i+1)
            if isValid(s[0:3]):
                cp3 = cur.copy() 
                cp3[i] = s[0:3]
                dp(s[3:], cp3, i+1)

        # start dp with initial s, fill the 0th slot/index of the array given.
        dp(s, [None, None, None, None], 0)

        # Convert subarrays into a string . separated
        res = []
        for arr in ans:
            res.append(".".join(arr))

        return res
        