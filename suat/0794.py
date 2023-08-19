class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        countX, countO = 0, 0
        # check the rule 1
        for s in board:
            for i in range(3):
                if s[i] == "X":
                    countX += 1
                elif s[i] == "O":
                    countO += 1
            print(countX, countO)
        if countX-countO > 1 or countX-countO < 0:
            return False

        xWins = self.isWinning("X", board)
        oWins = self.isWinning("O", board)

        # check rule 2
        if xWins and oWins:
            return False

        # check rule 3
        if xWins and countX-countO != 1:
            return False

        # check rule 4   
        if oWins and countX != countO:
            return False

        return True    


    def isWinning(self, c: str, b: List[str]) -> bool:
        #check rows for winner
        for i in range(3):
            if b[i][0] == b[i][1] and b[i][0] == b[i][2] and b[i][0] == c:
                return True
        #check columns for winner
        for i in range(3):
            if b[0][i] == b[1][i] and b[0][i] == b[2][i] and b[0][i] == c:
                return True
        # check crosses
        if b[0][0] == b[1][1] and b[0][0] == b[2][2] and b[0][0] == c:
            return True
        if b[0][2] == b[1][1] and b[0][2] == b[2][0] and b[0][2] == c:
            return True


'''
1. countX must be equal or +1 countO
2. both players can not be in a winner position at the same time
3. if X wins countX should be countO+1
4. if O wins countX = countO
'''