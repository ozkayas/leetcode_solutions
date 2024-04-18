class Solution:
    def calculate_edges(self, vector:List[int]) -> int:
        edges = 0 # 2
        onWater = True # True
        for p in vector:
            if onWater and p == 1: #We are stepping on a land
                edges += 1
                onWater = False
            elif not onWater and p == 0: # We are stepping on water
                edges += 1
                onWater = True
        
        if not onWater: ## Land is at the border, so add last edge
            edges += 1

        return edges

    def columnsOfMatrix(self, m:List[List[int]]) -> List[int]:
        R, C = len(m), len(m[0])
        # Get columns and edges
        columns = []
        # 00, 10, 20. 30
        for c in range(C):
            temp = []
            for r in range(R):
                temp.append(m[r][c])
            columns.append(temp) 

        return columns

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        ans = 0

        ## Loop for each row and column
        ## Count vertical and horizontal edges
        for row in grid:
            edges = self.calculate_edges(row)
            ans += edges

        for col in self.columnsOfMatrix(grid):
            edges = self.calculate_edges(col)
            ans += edges

        return ans
        