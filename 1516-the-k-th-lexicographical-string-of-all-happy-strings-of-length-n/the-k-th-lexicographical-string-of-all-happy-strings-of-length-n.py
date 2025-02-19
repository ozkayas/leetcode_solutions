class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        all = set()
        letters = ["a","b","c"]

        def generate(sublist:str):
            if len(sublist) == n:
                all.add(sublist)
                return
            
            for l in letters:
                if not sublist:
                    generate(l)
                elif sublist[-1] != l:
                    generate(sublist+l)
            

        generate("")
        allsorted = sorted(list(all))
        if len(allsorted) < k:
            return ""
        return allsorted[k-1]




        