class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def generate(o:int, c:int, current:str):
            if o == 0 and c == 0:
                ans.append(current)
                return
            
            if o == c:
                generate(o-1,c,current+"(")
            else:
                if o > 0:
                    generate(o-1,c,current+"(")
                generate(o,c-1,current+")")

        
        generate(n, n, "")

        return ans 