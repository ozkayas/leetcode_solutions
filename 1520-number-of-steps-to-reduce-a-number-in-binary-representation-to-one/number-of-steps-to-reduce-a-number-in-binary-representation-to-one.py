class Solution:

    def numSteps(self, s: str) -> int:
        s = list(s)
        ops= 0

        def divideByTwo(s: List[str]):
            s.pop()

        def addOne(s: List[str]):
            i = len(s) -1
            # Iterate while char = 1 and changing to 0
            while i >= 0 and s[i] == "1":
                s[i] = "0"
                i -= 1

            if i < 0:
                s.insert(0, "1")
            else:
                s[i] = "1"

        while len(s) > 1:
            N = len(s)
            if s[N-1] == "0":
                divideByTwo(s)
            else:
                addOne(s)
            ops += 1
        
        return ops
                
            


