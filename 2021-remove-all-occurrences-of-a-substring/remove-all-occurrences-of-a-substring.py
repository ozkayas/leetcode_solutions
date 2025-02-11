class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        lenS, lenP = len(s), len(part)
        st = []

        def checkPop():
            if len(st) < lenP:
                return
            if "".join(st[-lenP:]) == part:
                for _ in range(lenP):
                    st.pop()
            return

        for ch in s:
            st.append(ch)
            checkPop()

        return "".join(st)

        