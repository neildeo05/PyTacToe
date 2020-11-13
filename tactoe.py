import numpy as np
import random
class TicTacToe:
    def __init__(self):
        self.board = np.zeros(9)
        self.currMove = 0
        self.turn = 1
        self.over = False
        self.reward = 0
    def showBoard(self):
        return self.board.reshape(3,3)
    def clearBoard(self):
        self.board = np.zeros(9)
        self.over = False
        self.turn = 1;
        self.reward = 0
    def action(self, move):
        if(self.board[move]):
            self.reward = -1000
            self.over = True
        else:
            self.board[move] = self.turn
            self.turn = -1 * self.turn
            self.isWinner()
        return (self.showBoard(), self.over, self.reward)
    def isWinner(self):
        test_b = self.showBoard()
        if any([all(test_b[:,x] == 1) for x in range(3)]):
            self.over = True
            self.reward = 100
        elif any([all(test_b[x] == 1)for x in range (3)]):
            self.over = True
            self.reward = 100
        elif all(np.array([self.board[0],self.board[4],self.board[8]]) == 1):
            self.over = True
            self.reward = 100
        elif all(np.array([self.board[2], self.board[4], self.board[6]]) == 1):
            self.over = True
            self.reward = 100
            
            
        elif any([all(test_b[:,x] == -1) for x in range(3)]):
            self.over = True
            self.reward = -100
        elif any([all(test_b[x] == -1)for x in range (3)]):
            self.over = True
            self.reward = -100
        elif all(np.array([self.board[0],self.board[4],self.board[8]]) == -1):
            self.over = True
            self.reward = -100
        elif all(np.array([self.board[2], self.board[4], self.board[6]]) == -1):
            self.over = True
            self.reward = -100
        elif all(self.board):
            self.over = True
            self.reward = -100
        else:
            self.over=False

def play():
    env = TicTacToe()
    status = 100
    count = 0
    board,staus = 0, 0
    while True:
        while not env.over:
            board, _, status = env.action(random.randint(0,8))
            print(board)
            if status == -1000:
                env.clearBoard()
            elif(status == -100):
                print("LOSER")
                break
            elif status == 100:
                print("WINNER")
                break
        return board,status

def main():
    mat = np.zeros((3,3))
    print(play())

        
if __name__ == '__main__' :
    main()
