import copy

class Game:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.winnerVar = 0
        self.curPlayer = 1
        self.boardSize = 3
        self.moveHistory = []
        self.masterFC = 0
        self.player1 = None
        self.player2 = None

    def isBoardFull(self):
        boardFull = True
        for i in self.board:
            if i.count(0) > 0:
                boardFull = False
                break

        return boardFull

    def move(self, theInput):
        if theInput not in range(0, 9):
            return -2
        if self.board[theInput//3][theInput%3] == 0:
            self.board[theInput//3][theInput%3] = self.curPlayer
            self.moveHistory.append(theInput+1)
            return 1
        else:
            return -1

    # def move(self, theInput, fc):
    #     if theInput not in range(0, 9):
    #         return -2
    #     if self.board[theInput//3][theInput%3] == 0:
    #         self.board[theInput//3][theInput%3] = self.curPlayer
    #         # print("fc:", fc, " made move", theInput, "for player", self.curPlayer, "board: ", self.board)
    #         self.moveHistory.append(theInput)
    #         return 1
    #     else:
    #         return -1

    def clearMove(self, theInput):
        if theInput not in range(0, 9):
            return -2
        else:
            self.board[theInput//3][theInput%3] = 0
            return 1

    def getEmpties(self):
        empties = []
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if self.board[i][j] == 0:
                    empties.append((i*3)+j)
        return empties

    def getCopy(self):
        return copy.deepcopy(self)

    def checkForWinner(self):
        """
        INPUT:  a random list of lists containing ints like:
        [[int,int,int],[int,int,int],[int,int,int]]
        where int is between 0 and 2
    
        WORK: check to see if player 1 wins, player 2 wins, or no one wins
    
        OUTPUT:  return 0 if nobody wins, 1 if player one wins, 2 if player two wins.
        """
    
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != 0:
            return self.board[0][1]
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] != 0:
            return self.board[1][1]
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] != 0:
            return self.board[2][1]
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] != 0:
            return self.board[0][0]
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] != 0:
            return self.board[0][1]
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] != 0:
            return self.board[0][2]
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return self.board[0][2]
        else:
            return 0

    def drawTheBoard(self):
        topRow = ""
        bottomRow = ""
        count = 1
        drawnBoard = ""
        for i in self.board:
            for j in range(3):
                topRow += " ---"
            #print(topRow)
            drawnBoard += topRow + "\n"

            midRow = ""

            for j in i:
                if j == 1:
                    midRow += "| X "
                elif j == 2:
                    midRow += "| O "
                else:
                    midRow += "| " + str(count) + " "
                count += 1
            midRow += "|"
            # print(midRow)
            drawnBoard += midRow + "\n"

            topRow = ""
            bottomRow = ""

        for i in range(3):
            bottomRow += " ---"

        #print(bottomRow)
        drawnBoard += bottomRow
        return drawnBoard
