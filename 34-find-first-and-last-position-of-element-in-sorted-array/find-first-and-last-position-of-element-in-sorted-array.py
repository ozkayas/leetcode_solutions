class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        # we need 2 binary search
        # 2 3 3 4 5 8 8 8 8 9 9 10 
        #           s     e
        startIndex, endIndex = -1, -1
        ## 1 Binary Search for target <= middle
        ## To find starting of the target

        l, r = 0, N-1
        while l <= r:
            m = l + (r-l)//2

            if nums[m] >= target:
                # We are ok, but continue search the first appearance of the 8, or 9 ...
                startIndex = m
                r = m -1
            else:
                l = m +1
        if startIndex == -1 or nums[startIndex] != target:
            # BS ended but can not find the target, propably bigger than 8, target
            return [-1, -1]

        ## 2. Binary Search for middle <= target
        ## Last of the target
        l, r = startIndex, N -1 # we can start l from start index

        while l <= r:
            m = l + (r-l)//2

            if nums[m] <= target:
                # We are ok, but should search to the right
                endIndex = m
                l = m + 1
            else:
                r = m - 1

        return [startIndex, endIndex]