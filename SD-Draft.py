import numpy as np
import random
import math


# DEPRECATED, SEE SD-TACTOE FOR FINAL 

# x: 1
# o: -1
class TicTacToe:
    def __init__(self):
        self.board = np.zeros(9)
        self.dimension = 3
        self.lastValidIndex = self.dimension - 1
        self.over = False
        self.turn = 1

    # Reshapes it into the normal board shape (2D)
    def normalShape(self):
        return self.board.reshape(self.dimension, self.dimension)

    def action(self, move):
        # valid move will be when the index is less than the size, and the index is currently 0
        if self.spotsAvailable():
            print(self.spotsAvailable())
            while self.board[move] != 0:
                move = self.makeRandomMove()
                # print(self.normalShape())
                
            self.board[move] = self.turn
            self.turn = self.turn * -1

        print(self.normalShape())

        self.isWinner()

    def spotsAvailable(self):
        indexes = np.where(self.board == 0)
        return len(indexes) != 0

    @staticmethod
    def makeRandomMove():
        return random.randint(0, 8)

    def clearBoard(self):
        self.board = np.zeros(9)
        self.over = False
        self.turn = 1

    def checkHori(self, row, playerToCheck):
        if self.dimension > row:
            properView = self.normalShape()

            xHoriWin = np.array([1, 1, 1])
            yHoriWin = np.array([-1, -1, -1])

            toCheck = properView[row]

            if playerToCheck == "x":
                return np.array_equal(toCheck, xHoriWin)
            else:
                return np.array_equal(toCheck, yHoriWin)

        return False

    def checkVert(self, col, playerToCheck):
        if self.dimension > col:
            properView = self.normalShape()

            xVertWin = np.array(([1], [1], [1]))
            yVertWin = np.array(([-1], [-1], [-1]))

            toCheck = np.array(())
            for x in range(self.dimension):
                toAdd = properView[x][col]
                toCheck = np.append(toCheck, toAdd)

            if playerToCheck == "x":
                return np.array_equal(toCheck, xVertWin)
            else:
                return np.array_equal(toCheck, yVertWin)

        return False

    # dir = left: go from topL to bottomR - dir = right: go from topR to bottomL
    def checkDiag(self, direct, playerToCheck):
        properView = self.normalShape()

        xFlatWin = np.array((1, 1, 1))
        yFlatWin = np.array((-1, -1, -1))

        toCheck = np.array(())

        if direct == "left":
            toCheck = properView.diagonal()
        else:
            toCheck = np.fliplr(properView).diagonal()

        if playerToCheck == "x":
            return np.array_equal(toCheck, xFlatWin)
        else:
            return np.array_equal(toCheck, yFlatWin)

    def isWinner(self):
        # z means no one won
        winner = "z"

        for a in range(self.dimension):
            xWonDiag = self.checkDiag("left", "x") or self.checkDiag("right", "x")
            yWonDiag = self.checkDiag("left", "y") or self.checkDiag("right", "y")

            xWonStraight = self.checkHori(a, "x") or self.checkVert(a, "x")
            yWonStraight = self.checkHori(a, "y") or self.checkVert(a, "y")

            if xWonStraight or xWonDiag:
                winner = "x"
                break
            elif yWonStraight or yWonDiag:
                winner = "y"
                break

        if winner != "z":
            self.over = True
            if winner == "x":
                print("Comp1 Wins")
            else:
                print("Comp2 Wins")
        elif not self.spotsAvailable():
            self.over = True
            print("Draw")
            
        
        print("")

        if self.over:
            self.clearBoard()
            
            if input("Play Again?") == "y":
                print("Starting new game..\n\n")
                self.action(self.makeRandomMove())
            else:
                print("Thank you for playing.")


def play():
    game = TicTacToe()

    while not game.over:
        print("-------------")
        print()

        if game.turn == 1:
            print("Comp1's Turn")
        else:
            print("Comp2's Turn")

        print()

        # first call to start the game
        game.action(game.makeRandomMove())

    print()
    print("Game Over")


# MAKE SURE TO CALL play()
play()
