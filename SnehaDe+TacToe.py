import numpy as np
from numpy import random as r

# x: 1
# o: -1

def play():
    #this is where you will instantiate the TicTacToe class, and while no player has won, continue with the loop
    pass

# MAKE SURE TO CALL play()



class TicTacToe:
    def __init__(self):
        self.board = np.zeros(9)
        self.dimension = math.sqrt(self.board.shape)
        self.lastValidIndex = dimension - 1
        self.over = False
        self.turn = 1

    def action(self, move):
        # make sure to change the turn : self.turn = self.turn * -1
        # board[move] = turn

        #self.dimension * move[0] accounts for the row, move[1] is the col. adding these represents when the array is flat.
        self.board[self.dimension * move[0] + move[1]] = turn
        self.turn = self.turn * -1
        isWinner(self)

    def isWinner(self):
        # check each horizontal and vertical line, and check the diagonal.
        #there are 2 main ways to check the diagonal, easy way is to check them explicitly, and the harder way is to use np.eye(), np.fliplr(), and 
        #other ways to check the main diagonal with numpy
        pass
    
    def clearBoard(self):
        self.board = np.zeros(9)
        self.over = False
        self.turn = 1
        pass

    def checkHori(self, row, playerToCheck):
        if dimension > row:
            properView = normalShape(self)

            xHoriWin = np.array([1, 1, 1])
            yHoriWin = np.array([-1, -1, -1])

            toCheck = properView[row]

            if playerToCheck == "x":
                return np.array_equal(toCheck, xHoriWin)
            else:
                return np.array_equal(toCheck, yHoriWin)

        return False

    def checkVert(self, col, playerToCheck):
        if dimension > col:
            properView = normalShape(self)

            xVertWin = np.array(([1], [1], [1]))
            yVertWin = np.array(([-1], [-1], [-1]))

            toCheck = np.array(())
            for x in range(self.dimension):
                toAdd = properView[x][col]
                toCheck = numpy.append(toCheck, toAdd)

            if playerToCheck == "x":
                return np.array_equal(toCheck, xVertWin)
            else:
                return np.array_equal(toCheck, yVertWin)

        return False

    #dir = left: go from topL to bottomR - dir = right: go from topR to bottomL
    def checkDiag(self, dir, playerToCheck):
        properView = normalShape(self)
        
        xFlatWin = np.array((1, 1, 1))
        yFlatWin = np.array((-1, -1, -1))

        toCheck = np.array(())

        if dir == "left":
            toCheck = properView.diagonal()
        else:
            toCheck = np.fliplr(properView).diagonal()


        if playerToCheck == "x":
            return np.array_equal(toCheck, xFlatWin)
        else:
            return np.array_equal(toCheck, yFlatWin)


    #Reshapes it into the normal board shape (2D)
    def normalShape(self)
        return self.board.reshape(self.dimension, self.dimension)