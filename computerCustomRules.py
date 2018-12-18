import random

def pickSide(board):
    tempList = []
    if board[0][1] == 0:
        tempList.append((0, 1))
    if board[1][2] == 0:
        tempList.append((1, 2))
    if board[1][0] == 0:
        tempList.append((1, 0))
    if board[2][1] == 0:
        tempList.append((2, 1))
    if len(tempList) > 0:
        return random.choice(tempList)
    else:
        return 0

def computerPlayer(game):
    """INPUT: Gameboard and the Current curPlayer (int)
       WORK: Check board to be sure there is space left, check computer's choice, computer choose a space.
       OUTPUT: The board with the players choice added, or -1 if the board is full, or -2 if an error.
    """
    random.seed()
    # check for empty spaces
    if 0 not in game.board[0] and 0 not in game.board[1] and 0 not in game.board[2]:
        return -1
        # if no empty spaces, return -1

    # if only 1 space available, choose it
    if game.board[0].count(0) + game.board[1].count(0) + game.board[2].count(0) == 1:
        for i in range(3):
            for j in range(3):
                if game.board[i][j] == 0:
                    # game.move(i * 3 + j)
                    return i * 3 + j

    # check for computer win, choose win if available
    for i in range(3):
        for j in range(3):
            if game.board[i][j] == 0:
                # clone game.board to tempgame.board, set tempgame.board[i][j] = game.curPlayer
                tempBoard = game.getCopy()
                tempBoard.move(i * 3 + j)
                # then call checkForWinner(tempgame.board)
                tempWin = tempBoard.checkForWinner()
                # if win, then choose game.board[i][j] = game.curPlayer and return game.board
                if tempWin == game.curPlayer:
                    # game.move(i * 3 + j)
                    return i * 3 + j

    # check for opponent win, block win if available
    otherPlayer = game.curPlayer%2+1
    for i in range(3):
        for j in range(3):
            if game.board[i][j] == 0:
                tempBoard = game.getCopy()
                tempBoard.curPlayer = otherPlayer
                tempBoard.move(i * 3 + j)
                # then call checkForWinner(tempgame.board)
                tempWin = tempBoard.checkForWinner()
                # if win, then choose game.board[i][j] = game.curPlayer and return game.board
                if tempWin == otherPlayer:
                    # game.move(i * 3 + j)
                    return i * 3 + j

    # if second player, go for middle
    if game.curPlayer == 2:
        if game.board[1][1] == 0:
            # game.move(4)
            return 4

    # check for if opponent has one corner and nothing else, if so, pick center
    moveVar = 0
    for i in game.board:
        for j in i:
            if j == otherPlayer:
                moveVar += 1
    if moveVar == 1:
        if game.board[0][0] == otherPlayer or game.board[0][2] == otherPlayer or game.board[2][0] == otherPlayer or game.board[2][2] == otherPlayer:
            # game.move(4)
            return 4

    # check for if opponent has two corners, if so, pick side
    if moveVar == 2:
        if game.board[0][0] == otherPlayer:
            if game.board[0][2] == otherPlayer or game.board[2][0] == otherPlayer or game.board[2][2] == otherPlayer:
                side = pickSide(game.board)
                if side != 0:
                    # game.move(side[0]*3+side[1])
                    return side[0]*3+side[1]
        elif game.board[0][2] == otherPlayer:
            if game.board[2][0] == otherPlayer or game.board[2][2] == otherPlayer:
                side = pickSide(game.board)
                if side != 0:
                    # game.move(side[0] * 3 + side[1])
                    return side[0] * 3 + side[1]
        elif game.board[2][0] == otherPlayer:
            if game.board[2][2] == otherPlayer:
                side = pickSide(game.board)
                if side != 0:
                    # game.move(side[0] * 3 + side[1])
                    return side[0] * 3 + side[1]

    # check for if opponent has two sides next to each other, if so, pick corner between them
    if moveVar == 2:
        if game.board[0][1] == otherPlayer and game.board[1][0] == otherPlayer:
            # game.move(0)
            return 0
        elif game.board[0][1] == otherPlayer and game.board[1][2] == otherPlayer:
            # game.move(2)
            return 2
        elif game.board[2][1] == otherPlayer and game.board[1][0] == otherPlayer:
            # game.move(6)
            return 6
        elif game.board[2][1] == otherPlayer and game.board[1][2] == otherPlayer:
            # game.move(8)
            return 8

    # place in random corner
    tempList = []
    if game.board[0][0] == 0:
        tempList.append((0, 0))
    if game.board[0][2] == 0:
        tempList.append((0, 2))
    if game.board[2][0] == 0:
        tempList.append((2, 0))
    if game.board[2][2] == 0:
        tempList.append((2, 2))
    if len(tempList) > 0:
        tempChoice = random.choice(tempList)
        # game.move(tempChoice[0] * 3 + tempChoice[1])
        return tempChoice[0] * 3 + tempChoice[1]

    # place in middle
    if game.board[1][1] == 0:
        # game.move(4)
        return 4

    # finally, pick a side
    side = pickSide(game.board)
    if side != 0:
        # game.move(side[0] * 3 + side[1])
        return side[0] * 3 + side[1]

    return -2
