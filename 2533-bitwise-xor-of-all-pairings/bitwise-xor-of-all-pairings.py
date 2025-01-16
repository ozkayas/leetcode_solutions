class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)

        def xorNums(arr: List[int]) -> int:
            total = 0
            for n in arr:
                total = total ^ n
            return total

        if n1 % 2 == 0 and n2 %2 == 0:
            return 0
        
        if n1 % 2 == 0:
            return xorNums(nums1)
        if n2 % 2 == 0:
            return xorNums(nums2)
        else:
            return xorNums(nums1) ^ xorNums(nums2)
     