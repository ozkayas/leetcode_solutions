class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        lo, hi = 0, m

        while lo <= hi:
            mid = (lo + hi)//2
            k = (m+n)//2 - mid
            if mid > 0 and nums1[mid-1] > nums2[k]: hi = mid
            elif mid < m and nums1[mid] < nums2[k-1]: lo = mid+1
            else:
                if mid == m: right = nums2[k]
                elif k == n: right = nums1[mid]
                else: right = min(nums1[mid], nums2[k])

                if (m+n)%2: return right

                if mid == 0: left = nums2[k-1]
                elif k == 0: left = nums1[mid-1]
                else: left = max(nums1[mid-1], nums2[k-1])

                return (left + right)/2


'''
[1,2,4,6,7,8]
     |
     m

mid =  5 + 0 // 2 = 2 --> pointing to 4, mid is also the count of numbers before mid
remaining count of leftSide must come form the secont array.
so if
nums2 = [3,4,5]
leftSide = 4 numbers
numbers from nums2 = leftSide - m = 4 - 2, then index of mid2 is '2'

then we should check cross check of sliced arrays


'''

        