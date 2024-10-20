class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = []
        operators = {"&", "|", "!"}

        def handleOperation(op: str, bools: list) -> str:
            match op:
                case "&":
                    return "t" if "f" not in bools else "f"
                case "|":
                    return "t" if "t" in bools else "f"
                case "!":
                    return "t" if bools[0] == "f" else "f"


        for c in expression:
            if c != ")":
                st.append(c)
            else:
                # if we see bools inside paranthesis
                bools = []
                # pop values 1 by 1 until reacing an operator
                while st[-1] not in operators:
                    cur = st.pop()
                    if cur in ["t","f"]:
                        bools.append(cur)

                # pop the operator
                op = st.pop()
                subResult = handleOperation(op, bools)
                st.append(subResult)

        return True if st[0] == "t" else  False
        
        
"""
&(t, f
     ^

"""