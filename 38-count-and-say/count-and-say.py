class Solution:
    def countAndSay(self, n: int) -> str:
        
        def RLE(s:str) ->str:
            strBuilder = ""
            i = 0
            while i < len(s):
                curCh = s[i]
                chCounter = 0
                while i < len(s) and s[i] == curCh:
                    i += 1
                    chCounter += 1
                strBuilder += str(chCounter) + curCh
            return strBuilder
        
        cur = "1"
        while n-1:
            cur = RLE(cur)
            n -= 1

        return cur

        