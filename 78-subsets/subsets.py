class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def bt(i, subset):
            if i == len(nums):
                ans.append(subset.copy())
                return
            
            subset.append(nums[i])
            bt(i + 1, subset)
            subset.pop()
            bt(i + 1, subset)

        
        bt(0, [])

        return ans









    
        