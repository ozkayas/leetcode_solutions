class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends or target in deadends:
            return -1

        visited = set(deadends)
        ans = -1

        # takes a state of lock and returns all alternatives from this states
        def codesFrom(code:str)-> List[str]:   
            nonlocal visited

            toNext = {"0":"1","1":"2","2":"3","3":"4","4":"5","5":"6","6":"7","7":"8","8":"9","9":"0"}
            toPrev = {"1":"0","2":"1","3":"2","4":"3","5":"4","6":"5","7":"6","8":"7","9":"8","0":"9"}
            codeAsList = list(code)
            moves = []

            for i in range(len(code)):
                curr = code[i]

                nextCode = codeAsList[:]
                nextCode[i] = toNext[curr]
                nextCodeStr = "".join(nextCode)

                prevCode = codeAsList[:]
                prevCode[i] = toPrev[curr]
                prevCodeStr = "".join(prevCode)

                if nextCodeStr not in visited:
                    moves.append(nextCodeStr)
                if prevCodeStr not in visited:
                    moves.append(prevCodeStr)
            # print("moves from code:", code, moves)
            return moves

        ## TEST movesFrom
        # print(codesFrom("0201"))



        # Stack will hold the value and the bfs level
        bfsStack = deque()
        bfsStack.append(("0000", 0))
        
        while bfsStack:
            # print(bfsStack)
            curCode, curLevel = bfsStack.popleft()
            visited.add(curCode)

            if curCode == target:
                ans = curLevel
                break

            for code in codesFrom(curCode):
                # print("code", code)
                # print(visited)
                if code not in visited:
                    visited.add(code)
                    bfsStack.append((code,curLevel+1))


        return ans