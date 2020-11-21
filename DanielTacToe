import numpy as np


def charVal(x):
    if x == 0:
        return "_"
    elif x == 1:
        return "X"
    elif x == -1:
        return "O"


class TicTacToe:
    def __init__(self):
        self.board = np.zeros(9)
        self.over = False
        self.turn = -1
        self.count = 0

    def action(self, move):
        try:
            move = int(move)
        except ValueError:
            print("Invalid input.")
            self.action(input("Enter a number from 1 - 9: "))
            return

        if move < 1 or move > 9:
            print("Invalid input.")
            self.action(input("Enter a number from 1 - 9: "))
            return

        if self.board[move - 1] != 0:
            print("This spot has already been chosen.")
            self.action(input("Enter another number: "))
            return

        self.turn = self.turn * -1
        self.board[move - 1] = self.turn
        self.count += 1

    def checkWinner(self):
        b = self.board

        for i in np.arange(3):
            if (b[i * 3] == b[i * 3 + 1] and b[i * 3] == b[i * 3 + 2] and b[i * 3] != 0) \
                    or (b[i] == b[i + 3] and b[i] == b[i + 6] and b[i] != 0):
                self.over = True
                return

        if ((b[0] == b[4] and b[0] == b[8]) or (b[2] == b[4] and b[2] == b[6])) \
                and b[4] != 0:
            self.over = True
            return

        if self.count == 9:
            self.printBoard()
            print("No one won. :(")
            self.resetGame()

    def printBoard(self):
        for i in np.arange(3):
            for j in np.arange(3):
                print(charVal(self.board[i * 3 + j]), end=" ")
            print("")

    def resetGame(self):
        self.board = np.zeros(9)
        self.over = False
        self.turn = -1
        self.count = 0

        print("The game has been reset.")


def play():
    print("This is TicTacToe. The first player to have three-in-a-row wins.")
    print("These are the numbers that correspond to the spot on the grid: ")
    for i in np.arange(1, 10):
        print(str(i), end=" ")
        if i % 3 == 0:
            print()
    print()

    board = TicTacToe()
    while not board.over:
        board.printBoard()
        board.action(input("Enter a number (" + charVal(-board.turn) + "'s turn): "))
        board.checkWinner()

        if board.over:
            board.printBoard()
            print("The winner is " + str(charVal(board.turn)) + "! :)")

            if input("Would you like to play again(y/n)? ") == "y":
                board.resetGame()


if __name__ == '__main__':
    play()
