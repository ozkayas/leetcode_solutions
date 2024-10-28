class Solution:
    def maxArea(self, height: List[int]) -> int:
        def amount(lo, hi) -> int:
            return min(height[lo],height[hi]) * (hi-lo)


        lo , hi = 0, len(height)-1
        maxSoFar = 0



        while lo < hi:
            # calculate water here
            maxSoFar = max(maxSoFar, amount(lo,hi))

            # Shift shorter wall
            if height[lo] <= height[hi]:
                lo += 1
            else:
                hi -= 1
        return maxSoFar

        