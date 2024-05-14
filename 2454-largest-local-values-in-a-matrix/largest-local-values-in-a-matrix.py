class Solution:
    # Return the maximum values in the 3 x 3 matrix with top-left as (x, y).
    def find_max(self, grid, x, y):
        max_element = 0
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                max_element = max(max_element, grid[i][j])
        
        return max_element

    def largestLocal(self, grid):
        N = len(grid)
        
        max_local = [[0] * (N - 2) for _ in range(N - 2)]
        for i in range(N - 2):
            for j in range(N - 2):
                max_local[i][j] = self.find_max(grid, i, j)
        
        return max_local