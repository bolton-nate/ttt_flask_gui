from flask import Flask, render_template, request, redirect, url_for
from computerCustomRules import *
from computerRandom import *
from computerMinimax import *
from computerAlphaBeta import *
from Game import *

app = Flask(__name__)
ttt = Game()

@app.route('/start', methods=['GET'])
def start():
    return render_template('start.html')


@app.route('/turn1', methods=['POST'])
def firstplay():
    if request.form['p1'] in ['h','1','2','3','4']:
        ttt.player1 = request.form['p1']
        if request.form['p2'] in ['h', '1', '2', '3', '4']:
            ttt.player2 = request.form['p2']
            if ttt.player1 == 'h':
                return render_template('index.html',
                                   game=ttt,
                                   move=-1)
            else:
                if ttt.player1 == "1":
                    myMove = computerPlayer(ttt)
                elif ttt.player1 == "2":
                    myMove = computerRandom(ttt)
                elif ttt.player1 == "3":
                    myMove = computerMinimax(ttt)
                elif ttt.player1 == "4":
                    myMove = computerAlphaBeta(ttt)
                return render_template('index.html',
                                       game=ttt,
                                       move=myMove)
    return redirect(url_for('start'))


@app.route('/', methods=['GET'])
def main():
    global ttt
    if request.args.get('gameover') == "1":
        del ttt
        ttt = Game()
        return redirect(url_for('start'))
    if ttt.player1 is ttt.player2 is None:
        return redirect(url_for('start'))
    return render_template('index.html',
                           game=ttt,
                           move=-1)


@app.route("/", methods=['POST'])
def play():
    # process 'click'
    clicked = int(request.form['play'][0])
    ttt.move(clicked)
    # if we have a winner, set winnerVar and return to HTML
    if ttt.checkForWinner() > 0:
        ttt.winnerVar = ttt.checkForWinner()
        return render_template('index.html',
                               game=ttt,
                               move=-1)
    # next player
    ttt.curPlayer = ttt.curPlayer % 2 + 1
    # check if next player is computer, if so send computer's choice
    if (ttt.curPlayer == 1 and ttt.player1 != 'h') or (ttt.curPlayer == 2 and ttt.player2 != 'h'):
        if ttt.curPlayer == 1:
            if ttt.player1 == "1":
                myMove = computerPlayer(ttt)
            elif ttt.player1 == "2":
                myMove = computerRandom(ttt)
            elif ttt.player1 == "3":
                myMove = computerMinimax(ttt)
            elif ttt.player1 == "4":
                myMove = computerAlphaBeta(ttt)
        else:
            if ttt.player2 == "1":
                myMove = computerPlayer(ttt)
            elif ttt.player2 == "2":
                myMove = computerRandom(ttt)
            elif ttt.player2 == "3":
                myMove = computerMinimax(ttt)
            elif ttt.player2 == "4":
                myMove = computerAlphaBeta(ttt)
            if ttt.checkForWinner() > 0:
                ttt.winnerVar = ttt.checkForWinner()
    else: # otherwise it's a human and they'll make their own choice, return move=-1:
        myMove = -1
    # return to the HTML
    return render_template('index.html',
                           game=ttt,
                           move=myMove)


if __name__ == "__main__":
    app.run(debug=True)
