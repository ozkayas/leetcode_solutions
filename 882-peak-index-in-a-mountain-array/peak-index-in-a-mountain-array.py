class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        N = len(arr)

        def isPeak(i:int) -> bool:
            return arr[i-1] < arr[i] > arr[i+1]

        lo, hi = 1 , N-2
        while lo <= hi:
            mid = lo +(hi - lo)//2

            if isPeak(mid): return mid
            elif arr[mid-1] > arr[mid]: # peak is on the left
                hi = mid-1
            else: # peak is on the right
                lo = mid+1
            
        
        