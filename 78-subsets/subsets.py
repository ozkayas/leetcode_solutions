class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            for i in range(len(res)):
                newSubset = res[i] + [n]
                res.append(newSubset)
                


        return res
