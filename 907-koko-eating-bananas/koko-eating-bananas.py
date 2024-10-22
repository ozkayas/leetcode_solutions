class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Calculate how many hours needed for given k eating speed
        def calculateHours(k:int) -> int:
            h = 0
            for p in piles:
                h += math.ceil(p/k)
            return h

        piles.sort()
        lo, hi = 1 , piles[-1] 
        targetEatingSpeed = -1

        while lo <= hi:
            mid = lo + (hi-lo)//2
            hour = calculateHours(mid)
            if hour <= h: # koko eats within h, this is OK, but can slow down
                targetEatingSpeed = mid
                hi = mid -1
            else:
                lo = mid +1

        return targetEatingSpeed




"""
min: 1 max: 11
3 6 7 11

4 banana/hour -> helpermethod
def hours(speed) -> hours:



"""