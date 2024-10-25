class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A ,B = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        total_len = (len(A)+len(B))
        
        ### NOT Index, lenght of the portion
        lo, hi = 0, len(A)
        while lo <= hi:
            # length of portions from both arrays
            mid = lo + (hi - lo)//2
            k = (total_len+1)//2 - mid

            # edge values of sliced arrays
            maxLeftA = float("-inf") if mid == 0 else A[mid-1]
            minRightA = float("inf") if mid == len(A) else A[mid]
            maxLeftB = float("-inf") if k == 0 else B[k-1]
            minRightB = float("inf") if k == len(B) else B[k]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if total_len % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                else:
                    return max(maxLeftA, maxLeftB)

            elif maxLeftA > minRightB:
                hi = mid -1
            else:
                lo = mid +1






            
            


