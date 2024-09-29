class Solution:
    def minimumDeletions(self, s: str) -> int:
        st = []
        deleteCounter = 0

        for ch in s:
            if st and st[-1] == "b" and ch == "a":
                deleteCounter += 1
                st.pop()
            else:
                st.append(ch)
            
        return deleteCounter

        