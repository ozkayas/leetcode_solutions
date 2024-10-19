class Solution:
    def calculate(self, s: str) -> int:
        mulDiv = {"/" , "*"}
        addSub = {"+", "-"}

        def handleOp(prev, op, cur) -> str:
            print("operation: ", prev,op,cur)
            match op:
                case "*":
                    return str(int(prev)*int(cur))
                case "/":
                    if int(prev)*int(cur) < 0: # one of them is negative, round towards zero
                        return str(math.ceil(int(prev)/int(cur)))
                    else:
                        return str(math.floor(int(prev)/int(cur)))
                case "-":
                    return str(int(prev)-int(cur))
                case "+":
                    return str(int(prev)+int(cur))

        st = []
        # First pass
        curNum = []
        for c in s:
            if c == " ": continue
            if c.isdigit():
                curNum.append(c)
            else:
                st.append("".join(curNum)) # append num
                st.append(c) # append operator
                curNum.clear()
        if curNum: st.append("".join(curNum))
        # print(st)

        # second pass
        # st only holds values this time, not operators
        ans = []
        op = "+"
        for item in st:
            if item.isdigit():
                match op:
                    case "+":
                        ans.append(int(item))
                    case "-":
                        ans.append(-int(item))
                    case _:
                        prev = ans.pop()
                        ans.append(int(handleOp(prev,op,item)))
            else: # item is an operator
                op = item
        # print(ans)
        return sum(ans)