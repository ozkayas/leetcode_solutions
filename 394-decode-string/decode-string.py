class Solution:
    def decodeString(self, s: str) -> str:
        repeater = []
        st = []

        # helper method to process values between [] and repeat,
        def processChars() -> str:
            buffer = []
            while st[-1] != "[":
                buffer.append( st.pop() )
            st.pop() # pop [
            repeat = repeater.pop()
            return "".join(reversed(buffer)) * repeat

        tempNum = ""
        for ch in s:
            if ch.isdigit():
                tempNum += ch
            elif ch == "[":
                # There should be a num just before this. Process it
                repeater.append(int(tempNum))
                tempNum = ""
                st.append(ch)
            elif ch == "]":
                s = processChars()
                st.append(s)
            else:
                st.append(ch)

        return "".join(st)

        