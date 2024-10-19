class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def invert(s:str) -> str:
            temp = []
            for ch in s:
                temp.append("1" if ch == "0" else "0")
            return "".join(temp)

        def builder(n: int) -> str:
            if n == 1:
                return "0"
            else:
                prev = builder(n-1)
                return prev + "1" + invert(prev)[::-1]
        
        return builder(n)[k-1]
                
        