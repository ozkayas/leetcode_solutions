class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        p = 0  # pointer for spaces
        output = []
        for i in range(len(s)):
            if p < len(spaces) and i == spaces[p]:
                output.append(" ")
                p += 1
            output.append(s[i])


        return "".join(output)


        