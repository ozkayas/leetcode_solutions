class Solution:
    def minLength(self, s: str) -> int:
        st = [s[0]]
        for ch in s[1:]:
            if ch == "B" and st and st[-1] == "A":
                st.pop()
            elif ch == "D" and st and st[-1] == "C":
                st.pop()
            else:
                st.append(ch)
        
        return len(st) 

        