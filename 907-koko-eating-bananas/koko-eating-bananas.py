class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        def hour_for_k(k:int) -> int:
            h = 0
            for p in piles:
                h += math.ceil(p/k)
            return h

        ### Binary Search for each possible k
        l, r = 1, piles[-1]

        while l <= r:
            k = (l+r)//2

            if hour_for_k(k) > h: # KOKO is slow, we must find a bigger k
                l = k + 1
            else:
                r = k - 1

        return r+1



'''    
# Calculate hour for a pile
h:
    
   [4, 11, 20, 23, 30]  h = 6
    i                   -> ceils of 4/4 + 11/4 + 20/4 + 23/4 + 30/4 needed_hour

    
  
  '''