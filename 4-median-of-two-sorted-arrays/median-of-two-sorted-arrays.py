class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted(nums1+nums2)
        N = len(arr)
        print(arr)
        
        isEven = True if N % 2 == 0 else False
        
        median = 0
        if isEven:
            median = (arr[int((N-1)/2)]+ arr[int(N/2)]) / 2
        else:
            median = arr[int((N-1)/2)]

        return median 
