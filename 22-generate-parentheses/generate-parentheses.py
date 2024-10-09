class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def generate(o:int, c:int, subString):
            if o == 0 and c == 0:
                output.append(subString)
                return

            if o == c:
                generate(o-1,c, subString +"(")
            else:
                if o > 0:
                    generate(o-1,c, subString +"(")
                generate(o, c-1, subString +")")


        generate(n, n, "")

        return output
        