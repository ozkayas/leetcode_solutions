class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        N = len(s)

        def toList(s: str) -> list:
            t_list = [0 for _ in range(26)]
            for ch in s:
                ch_idx = ord(ch) - ord("a")
                t_list[ch_idx] += 1
            return t_list
        
        def updateList(old:list, removed:str, added:str) -> list:
            rem_idx = ord(removed) - ord("a")
            added_idx = ord(added) - ord("a")
            old[rem_idx] -= 1
            old[added_idx] += 1
            return old

        
        target = toList(p)
        ans = []
        for i in range(N - len(p)+1):
            if i == 0:
                subValue = toList(s[i:i+len(p)])
            else:
                subValue = updateList(subValue, s[i-1], s[i+len(p)-1])
            if subValue == target:
                ans.append(i)
            

        return ans
            


        