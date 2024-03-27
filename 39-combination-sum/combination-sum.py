class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def bt(i, curSum, comb):
            if i == len(candidates):return
            curVal = candidates[i]
            if curSum + curVal == target:
                comb.append(curVal)
                ans.append(comb.copy())
                comb.pop()
                return
            elif curSum + curVal > target:
                return
            
            else:
                comb.append(curVal)
                bt(i, curSum + curVal, comb)
                comb.pop()
                bt(i+1, curSum, comb)


            
        bt(0, 0, [])
        
        return ans