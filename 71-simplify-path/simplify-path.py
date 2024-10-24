class Solution:
    def simplifyPath(self, path: str) -> str:
        #replace / with " "
        emptyFilled = path.replace("/"," ")
        folders = emptyFilled.split()
        print(folders)

        st = []
        for f in folders:
            match f:
                case ".":
                    continue
                case "..":
                    if st: st.pop()
                case _:
                    st.append(f)
        
        return "/"+"/".join(st)
        