class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if len(strs) == 0: return res

        for i in range(len(strs[0])):
            cur = strs[0][i]
            for word in strs[1:]:
                if i == len(word) or (word[i] != cur):
                    return res
                
            res += cur
        
        return res
