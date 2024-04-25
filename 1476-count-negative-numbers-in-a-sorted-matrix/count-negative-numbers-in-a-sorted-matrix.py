class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        # for each row we should find the first negative, means target < 0 condition
        # [1,1,-1,-2]
        #  f f  t  t. -> find the first true

        # Takes a row and returns the first negative using binary search
        def indexOfNegative(row: List[int])-> int:
            N = len(row)
            if row[-1] >= 0: return N

            l, r = 0, N - 1
            ans = N

            while l <= r:
                m = l + (r-l)//2
                
                if row[m] <= -1: # OR row[m] < 0
                    # we are ok but look if any other on the left, so crop right
                    ans = m
                    r = m - 1
                else:
                    l = m + 1

            return ans

        counter = 0
        C = len(grid[0]) # number of columns

        for row in grid:
            firstNegative = indexOfNegative(row)
            # print(firstNegative)
            counter += C - firstNegative
        
        return counter