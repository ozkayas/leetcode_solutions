class Solution:
    ## Jumping indices of the table, values not used !!!, just index values as an array
    # [0, 14, 2, 3, 4, ... 34, 35]
    def boardToArr(self, board) -> List[int]:
        R, C = len(board), len(board[0])
        # Convert table to array
        readingRowToRight = True
        arr = []
        counter = 0

        for r in reversed(range(R)):
            if readingRowToRight:
                for c in range(C):
                    if board[r][c] == -1:
                        arr.append(counter)
                    else:
                        arr.append(board[r][c]-1)
                    counter += 1
                readingRowToRight = False
            else:
                for c in reversed(range(C)):
                    if board[r][c] == -1:
                        arr.append(counter)
                    else:
                        arr.append(board[r][c]-1)
                    counter += 1
                readingRowToRight = True
        print(arr)
        return arr

    def getAdjList(self, boardArr) -> dict:
        m, N = dict(), len(boardArr)
        for i in range(N):
            limit = min(i+7, N)
            m[i] = boardArr[i+1:limit]
        # print(m)
        return m

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        boardArr = self.boardToArr(board)
        adjList = self.getAdjList(boardArr)
        # print(boardArr)

        # holds (cell, step)
        bfs = deque([(0, 0)])
        visited = set({0})
        target = len(boardArr)-1

        while bfs:
            i, step = bfs.popleft()
            # print(f"i: {i}, step: {step}")
            if i >= target:
                return step

            for n in adjList[i]:
                # if not visited this index before, try to explore this 
                if n not in visited:
                    visited.add(n)
                    bfs.append((n, step+1))
        return -1
