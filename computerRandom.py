from random import choice, seed

def computerRandom(game):
    """INPUT: Gameboard and the Current curPlayer (int)
       WORK: get empty spaces and randomly choose a space
       OUTPUT: one of the empty spaces.
    """
    seed()
    myMove = choice(game.getEmpties())
    # print("My random move:", myMove + 1)
    # game.move(myMove)
    return myMove