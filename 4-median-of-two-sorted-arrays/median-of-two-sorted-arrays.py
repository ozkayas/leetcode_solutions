class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N1, N2 = len(nums1), len(nums2)
        # Assum nums1 shorter
        if N1 > N2:
            return self.findMedianSortedArrays(nums2, nums1)
        tot_len = N1 + N2

        lo, hi = 0, N1 # Not index, lengths
        while lo <= hi:
            l1 = lo + (hi-lo)//2
            l2 = (tot_len + 1)//2 - l1
        
            maxLeft1 = float("-inf") if l1 == 0 else nums1[l1-1]
            maxLeft2 = float("-inf") if l2 == 0 else nums2[l2-1]
            minRight1 = float("inf") if l1 == N1 else nums1[l1]
            minRight2 = float("inf") if l2 == N2 else nums2[l2]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if tot_len % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                hi = l1-1
            else:
                lo = l1 + 1