class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = numRows
        if n == 1: return s
        arr = [[] for _ in range(n)]
        diff = -1
        curRow = 0
        res = ""
        
        def changeDir():
            nonlocal diff
            diff = -1 * diff
            # print("changed dir to: ", diff)

        for i in range(len(s)):
            arr[curRow].append(s[i])           

            if i % (n-1) == 0:
                changeDir()
            curRow += diff
        
        for ar in arr:
            res += "".join(ar)

        # print(arr)
        return res


