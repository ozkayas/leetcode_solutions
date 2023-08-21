class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i = 0  #row index column index
        isDown = True
        result = ""

        if numRows == 1:
            return s


        m = ["" for x in range(numRows)]

        for c in s:
            if i == 0:
                isDown = True
            elif i == numRows-1:
                isDown = False
            m[i] += c 

            i = i + 1 if isDown else i -1

        for row in m:
            result += row

        return result