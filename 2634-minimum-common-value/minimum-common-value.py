class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)

        for num in nums2:
            if num in set1:
                return num
        
        return -1
        