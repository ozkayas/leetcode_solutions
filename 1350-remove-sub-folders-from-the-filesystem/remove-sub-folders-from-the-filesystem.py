class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        ans = []
        for f in folder:
            isSub = False
            for seen in ans:
                if f.startswith(seen+"/"):
                    isSub = True
                    break
            if not isSub:
                ans.append(f)


        return list(ans)

        