class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ## BFS and find groups, like union-find, add (r,c) tuples in group
        # Then traverse 0's and look neighbors to connect from different groups
        # size of each group
        groupSize = defaultdict(int)
        group = dict() # {(0,0):1 -> cell:group}
        maxArea = 0
        R, C = len(grid), len(grid[0])

        def canExplore(r,c) ->bool:
            return 0 <= r < R and 0 <= c < C and grid[r][c] == 1
        def canConnect(r,c) ->bool:
            return 0 <= r < R and 0 <= c < C and grid[r][c] == 2

        def explore(r,c,stamp):
            grid[r][c] = 2 # convert it to 2, instead of using a visited set
            group[(r,c)] = stamp
            groupSize[stamp] += 1
            for rr, cc in (r+1,c),(r-1,c),(r,c-1),(r,c+1):
                if canExplore(rr,cc):
                    explore(rr,cc,stamp)

        groupStamp = 0
        # Fill group table
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    groupStamp += 1
                    explore(r,c, groupStamp)

        # Traverse 0's, try to bridge groups
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    neighbors = set() # group
                    north, south, east, west = 0, 0, 0, 0
                    for rr, cc in (r+1,c),(r-1,c),(r,c-1),(r,c+1):
                        if canConnect(rr,cc):
                            neighbors.add(group[(rr,cc)])
                    totalArea = 1
                    for nei in neighbors:
                        totalArea += groupSize[nei]
                    maxArea = max(maxArea, totalArea)
    
        # if no 0'a exists return the maximum island
        maxIsland = max(groupSize.values()) if groupSize else 0
        return max(maxArea, maxIsland)