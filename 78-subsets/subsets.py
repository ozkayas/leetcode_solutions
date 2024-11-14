class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        def dfs(i:int, subSet):
            if i == len(nums):
                ans.append(subSet.copy())
                return
            dfs(i+1, subSet)
            subSet.append(nums[i])
            dfs(i+1, subSet)
            subSet.pop()

        dfs(0, [])

        return ans
        