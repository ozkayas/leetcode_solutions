class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pf = nums[0]
        mx = nums[0]
        for i in range(1, len(nums)):
            pf = max(pf+nums[i], nums[i])
            mx = max(mx, pf)

        return mx
            


"""
1, 4, 5, 6 ,
[-2, 1,-3, 4,-1, 2, 1,-5, 4]
 -2  1 -2  4  3  5  6  1  5  
 
"""