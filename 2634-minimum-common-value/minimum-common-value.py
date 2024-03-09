class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        p1 = p2 = 0

        while p1 < len(nums1) and p2 < len(nums2):
            n1, n2  = nums1[p1], nums2[p2]
            if n1 == n2:
                return n2
            
            if n1 <= n2:
                p1 += 1
            else:
                p2 += 1
        
        return -1



'''   
        set1 = set(nums1)

        for num in nums2:
            if num in set1:
                return num
        
        return -1
'''        