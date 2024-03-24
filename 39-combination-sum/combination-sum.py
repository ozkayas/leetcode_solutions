class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        
        def dfs(i, target, comb):
            if target == 0:
                ans.append(comb.copy())
                return
            if i >= len(candidates) or candidates[i] > target:
                return
            cur = candidates[i]
            
            comb.append(cur)
            dfs(i, target - cur, comb)
            comb.pop()
            dfs(i+1, target , comb)

        dfs(0, target, [])        
        return ans
        