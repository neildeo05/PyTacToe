import numpy as np
import random as r
import math

# Sneha De

# Computer 1 - 1
# Computer 2 - -1

SIZE = 9
player1Name = "CPU1"
player2Name = "CPU2"
spacer = "-----"
tab = "\t"

class TicTacToe:
    def __init__(self):
        self.board = np.zeros(SIZE)
        self.dimension = int(math.sqrt(self.board.size))
        self.over = False
        self.turn = 1
        self.numMovesDone = 0

    # Reshapes it into the normal board shape (2D)
    def normalShape(self):
        return self.board.reshape(self.dimension, self.dimension)

    @staticmethod
    def makeRandomMove():
        return r.randint(0, SIZE - 1)

    def clearBoard(self):
        self.board = np.zeros(SIZE)
        self.over = False
        self.turn = 1
        self.numMovesDone = 0

    def canPlaceMove(self):
        return self.numMovesDone < self.board.size

    def action(self):
        if self.canPlaceMove():
            # move is the index within a 1-D array.
            move = self.makeRandomMove()

            # find a blank spot to place a turn
            while self.board[move] != 0:
                move = self.makeRandomMove()

            self.board[move] = self.turn
            self.turn = self.turn * -1
            self.numMovesDone += 1

        self.isWinner()

    def isWinner(self):
        # z means no one won
        winner = "z"

        winners = np.array(
            [self.checkHori(), self.checkVert(), self.checkDiag()])

        # If any of the above results in a winner, change the variable
        if np.any(winners == "x"):
            winner = "x"
        elif np.any(winners == "y"):
            winner = "y"

        print(self.normalShape())

        # If a winner is found, announce it.
        # Or, if there are no more moves left, call a draw
        if winner != "z" or not self.numMovesDone < self.board.size:
            self.over = True

            print()
            formatPrint("GAME OVER")

            if winner == "x":
                formatPrint(player1Name + " WINS")
            elif winner == "y":
                formatPrint(player2Name + " WINS")
            else:
                formatPrint("DRAW")

    def checkHori(self):
        properView = self.normalShape()

        for x in range(self.dimension):
            # get the xth row
            extract = properView[x]

            if np.all(extract == 1):
                return "x"
            elif np.all(extract == -1):
                return "y"

        return "none"

    def checkVert(self):
        properView = self.normalShape()

        for x in range(self.dimension):
            # get the xth column
            extract = properView[:, x]

            if np.all(extract == 1):
                return "x"
            elif np.all(extract == -1):
                return "y"

        return "none"

    def checkDiag(self):
        properView = self.normalShape()

        fromLeft = properView.diagonal()
        fromRight = np.fliplr(properView).diagonal()

        if np.all(fromLeft == 1) or np.all(fromRight == 1):
            return "x"
        elif np.all(fromLeft == -1) or np.all(fromRight == -1):
            return "y"

        return "none"


# Formats printing as dash + tab + string + tab + dash
def formatPrint(string):
    print(spacer + tab + string + tab + spacer)

def play():
    game = TicTacToe()

    while True:
        print()
        if game.turn == 1:
            formatPrint(player1Name + "'S TURN")
        else:
            formatPrint(player2Name + "'S TURN")
        print()

        game.action()

        if game.over:
            game.clearBoard()

            print()
            if input("PLAY AGAIN? \n[y for yes, anything else to quit]: ") == "y":
                print("\nSTARTING NEW GAME..\n\n")
                game.action()
            else:
                print("\n\nTHANK YOU FOR PLAYING")
                break


play()
