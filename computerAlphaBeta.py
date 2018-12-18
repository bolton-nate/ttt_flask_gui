from random import randint, seed

def alphabeta(newGame, game, alpha, beta):
    global fc
    fc += 1
    game.masterFC += 1

    empties = newGame.getEmpties()
    # print("fc:", fc, " empties: ", empties)

    if newGame.checkForWinner() == game.curPlayer:
        # print("fc:", fc, " player win return 10")
        return -1, 100
    elif newGame.checkForWinner() == game.curPlayer % 2 + 1:
        # print("fc:", fc, " other player win return -10")
        return -1, -100
    elif not empties:
        # print("fc:", fc, " empty, return 0")
        return -1, -5

    bestMove = None
    if newGame.curPlayer == game.curPlayer:
        bestScore = -10000
        for i in empties:
            # advance the newGame to create a child node
            newGame.move(i)
            newGame.curPlayer = newGame.curPlayer % 2 + 1
            # find minimax of this child
            result = alphabeta(newGame, game, alpha, beta)
            # put newGame back in preparation for the next child node
            newGame.clearMove(i)
            newGame.curPlayer = newGame.curPlayer % 2 + 1
            # pick the max of the current bestScore or new score from child nodes
            if result[1] > bestScore:
                bestScore = result[1]
                bestMove = i
                # print("fc:", fc, " Max bestScore now: ", bestScore)
            # alpha beta pruning
            alpha = max(bestScore, alpha)
            if beta <= alpha:
                break
    else:
        bestScore = 10000
        for i in empties:
            # advance the newGame to create a child node
            newGame.move(i)
            newGame.curPlayer = newGame.curPlayer % 2 + 1
            # find minimax of this child
            result = alphabeta(newGame, game, alpha, beta)
            # put newGame back in preparation for the next child node
            newGame.clearMove(i)
            newGame.curPlayer = newGame.curPlayer % 2 + 1
            # pick the max of the current bestScore or new score from child nodes
            if result[1] < bestScore:
                bestScore = result[1]
                bestMove = i
                # print("fc:", fc, " Max bestScore now: ", bestScore)
            # alpha beta pruning
            beta = min(bestScore, beta)
            if beta <= alpha:
                break
    # print("fc:", fc, " returning bestmove/bestscore: ", bestMove, bestScore)
    return bestMove, bestScore



def computerAlphaBeta(game):
    global fc
    fc = 0
    newGame = game.getCopy()
    # if minimax is playing first, it spends forever and always picks top left.
    # instead, make first choice random for variability and time savings
    if len(game.getEmpties()) == 9:
        seed()
        # myMove = [0, None]
        myMove = [randint(0, 8), None]
    else:
        myMove = alphabeta(newGame, game, -float('inf'), float('inf'))
    # print("My minimax move:", myMove[0]+1)
    # game.move(myMove[0])
    return myMove[0]
