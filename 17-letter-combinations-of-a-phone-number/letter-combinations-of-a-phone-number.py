class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        cMap = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        ans = []
        def dfs(num:int, subSet:str):
            if num == len(digits):
                if subSet:
                    ans.append(subSet)
                return
            
            for ch in cMap[digits[num]]:
                dfs(num+1, subSet+ch)


        dfs(0, "")
        return ans
