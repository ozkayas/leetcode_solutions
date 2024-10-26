class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # directions[0] gives the current direction
        directions = deque([(0,1),(1,0),(0,-1),(-1,0)])

        R, C = len(matrix), len(matrix[0])

        def isValid(r, c) -> bool:
            return 0 <= r < R and 0 <= c < C and matrix[r][c] != None

        def nextCell(r, c) -> tuple:
            tryCount = 1
            while tryCount < 5 and not isValid(r +directions[0][0], c +directions[0][1]):
                tryCount += 1
                directions.append(directions.popleft())
            return (r +directions[0][0], c +directions[0][1]) if tryCount < 5 else None
            # dr, dc = directions[0]
            # if isValid(r+dr, c+dc):
            #     return (r+dr, c+dc)
            # else: # change direction
            #     directions.append(directions.popleft())
            #     dr, dc = directions[0]
            #     if isValid(r+dr,c+dc):
            #         return (r+dr, c+dc)
            #     else:
            #         return None


        ans = []
        def explore(r, c):
            ans.append(matrix[r][c])
            matrix[r][c] = None # mark as visited by setting to none

            nextRC = nextCell(r,c)
            if not nextRC:
                return
            else:
                rr, cc = nextRC
                explore(rr,cc)


        explore(0, 0)
        return ans

        