class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        output = []

        temp = []
        for ch in s:
            temp.append(ch)
            if len(temp) == k:
                output.append("".join(temp))
                temp.clear()
        
        if temp:
            while len(temp) < k:
                temp.append(fill)
            output.append("".join(temp))

        return output
        