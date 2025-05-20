class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def daysForCapacity(c:int) -> int: # Gives the days required for the given capacity
            total = 0
            days = 0
            for w in weights:
                if (total + w) > c:
                    days += 1
                    total = w
                else:
                    total += w
            return days+1


        lo, hi = max(weights), sum(weights)
        bestSoFar = hi
        while lo <= hi:
            mid = lo + (hi-lo)//2

            if daysForCapacity(mid) > days: # not good we should have a bigger ship
                lo = mid + 1
            else:
                bestSoFar = mid
                hi = mid -1
            
        return bestSoFar


        