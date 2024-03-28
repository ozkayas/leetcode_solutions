class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        N = len(nums)
        nums.sort()

        def dfs(i, subset):
            #we are out of bound, check and return
            if i == N:
                ans.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()

            while i+1 < N and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, subset)


        
        dfs(0, [])
        return ans 