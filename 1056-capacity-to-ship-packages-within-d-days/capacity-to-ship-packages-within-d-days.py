class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        # helper method, calculate the required days for a given ship capacity
        def countDays(capacity: int)-> int:
            days = 0
            temp = 0
            for w in weights:
                if w + temp > capacity:
                    days += 1
                    temp = w
                else:
                    temp += w

            return days + 1
            

        
        # Binary search between 10 - 55 // first Example
        # Can extract as a helper method, for O(N)
        lo, hi = max(weights), sum(weights)

        # Best ship capacity so far, we are trying to minimize it
        bestSoFar = hi
        while lo <= hi:
            mid = lo + (hi-lo)//2

            if countDays(mid) <= days:
                # This is good, this capacity [mid] is ok. lets save it and continue for a better one
                bestSoFar = mid
                hi = mid - 1
            else:
                lo = mid + 1


        return bestSoFar




        