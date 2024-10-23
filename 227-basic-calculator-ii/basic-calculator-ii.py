class Solution:
    def calculate(self, s: str) -> int:
        s = s + "." # Adding a dummy char so the last digit will be processed
        def handleOp(prev, nxt, op):
            if op == "*":
                return prev * nxt
            else:
                val = prev/nxt
                return math.ceil(val) if val < 0 else math.floor(val) 

        op = "+"
        st = []

        temp = 0
        for ch in s:
            if ch == " ": continue
            if ch.isdigit():
                temp = temp*10 + int(ch)
            else:
                # see a new operator
                if op in ["+", "-"]:
                    st.append(temp if op == "+" else -temp)
                else:
                    st.append(handleOp(st.pop(),temp, op))
                op = ch
                temp = 0
        
        return sum(st)




        