class Solution:
    def minLengthAfterRemovals(self, nums: list[int]) -> int:
        N = len(nums)
        l, r = N//2 -1 , N-1
        removed = 0

        while l >= 0:
            if nums[r] > nums[l]:
                removed += 2
                r -= 1
            l -= 1
        
        return N - removed
            






'''

1 1 3 3 5 5 

'''
        