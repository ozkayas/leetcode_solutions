class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Her hareketi 0/bos tasi bir yere kaydirma gibi dusunup bfs ile baslangictan-> target gitmeye calis
        # State => board verisinin stringe cevrilmis hali
        directions = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [2, 4],
        ]
        
        def _swap(state, i, j):
            state_list = list(state)
            state_list[i], state_list[j] = state_list[j], state_list[i]
            return "".join(state_list)

        target = "123450"
        initial_state = "".join(str(n) for row in board for n in row)

        bfsQ = deque([initial_state])
        visited = {initial_state}
        moves = 0

        while bfsQ:
            for _ in range(len(bfsQ)):
                curState = bfsQ.popleft()

                if curState == target:
                    return moves
                
                #where s zero in this state
                zeroPos = curState.index("0")
                for newPos in directions[zeroPos]:
                    nextState = _swap(curState, zeroPos, newPos)

                    if nextState in visited:
                        continue
                    visited.add(nextState)
                    bfsQ.append(nextState)
            moves += 1
        
        return -1


