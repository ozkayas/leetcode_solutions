class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        bits = list(s)
        res = ["0" for _ in s]
        res[-1] = "1"
        ones = -1 #Ones to replace at the head of the res

        for b in bits:
            if b == "1":
                ones += 1
        
        for i in range(ones):
            res[i] = "1"
        
        return "".join(res)

        