'''
You will create a file called <yourname>+TacToe.py
Create a TicTacToe class
In the TicTacToe class, there will be methods for:
    Create a board
    Render the board
    return true if the player has won
    Play a game
And whatever else you seem fit to be in your tictactoe class

Follow the github handbook to upload your file to the repository. Your code will be rejected if it doesn't work correctly

Here is a template you can follow
'''

import numpy as np
class TicTacToe:
    def __init__(self):
        self.board = np.zeros(9)
        self.over = False
        self.turn = 1
    def action(self, move):
        # make sure to change the turn : self.turn = self.turn * -1
        # board[move] = turn
        pass
    def isWinner(self):
        # check each horizontal and vertical line, and check the diagonal.
        #there are 2 main ways to check the diagonal, easy way is to check them explicitly, and the harder way is to use np.eye(), np.fliplr(), and 
        #other ways to check the main diagonal with numpy
        pass
    def clearBoard(self):
        #reset every instance variable
        pass


def play():
    #this is where you will instantiate the TicTacToe class, and while no player has won, continue with the loop
    pass

# MAKE SURE TO CALL play()

