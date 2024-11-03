class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        buckets = [deque() for _ in range(numRows)]
        i = 0
        forward = True # to reverse the direction of writing

        def updateI():
            nonlocal i, forward
            if forward:
                if i == numRows - 1:
                    forward = False
                    i -= 1
                else: 
                    i += 1
            else:
                if i == 0:
                    forward = True
                    i += 1
                else: 
                    i -= 1
        for ch in s:
            # process
            buckets[i].append(ch)
            updateI()

        output = []
        for bucket in buckets:
            output.extend(bucket)

        return "".join(output)

"""
"PAYPALISHIRING"
4 deques:
0:PIN
1:ALsiG
2:YAHR
3:PI

"""