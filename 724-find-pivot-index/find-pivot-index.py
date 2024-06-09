class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        preFix = 0

        for i,n in enumerate(nums):
            if preFix == (S-n)/2:
                return i
            else:
                preFix += n
        
        return -1
        
