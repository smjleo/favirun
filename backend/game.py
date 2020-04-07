import random
import os
import time

class Game:
    def __init__(self):
       self.reset() 

    def reset(self):
        self.board = [  # 0: empty
            [0, 0, 0],  # 1: obstacle
            [0, 0, 0],  # 2: player
            [0, 0, 0],
            [2, 0, 0]
        ]
        self.pos = 0    # position of player
        self.score = 0
        self.alive = True   

    def moveleft(self):
        if not self.alive:
            return
        if self.pos == 0:
            # can't go further
            return
        self.board[3][self.pos] = 0
        self.pos -= 1
        if self.board[3][self.pos] == 1:
            # hit obstacle
            self.dieSequence()
            return
        self.board[3][self.pos] = 2

    def moveright(self):
        if not self.alive:
            return
        if self.pos == 2:
            # can't go further
            return
        self.board[3][self.pos] = 0
        self.pos += 1 
        if self.board[3][self.pos] == 1:
            # hit obstacle
            self.dieSequence()
            return
        self.board[3][self.pos] = 2

    def advance(self):
        if not self.alive:
            return
        obstaclePos = random.randint(0, 2)  # next obstacle position
        # in some cases, some positions may be impossible
        # for example, you can't go through[1, 0, 0], [0, 1, 0], [0, 0, 1] without getting hit
        # i avoid this below:
        if (self.board[0][1] == 1 and self.board[1][2] == 1):
            obstaclePos = 2
        # same thing in reverse:
        if (self.board[0][1] == 1 and self.board[1][0] == 1):
            obstaclePos = 0
        self.board = [[0, 0, 0]] + self.board[:-1]  # move everything down, cut last element, add empty list to front
        self.board[0][obstaclePos] = 1  
        if self.board[3][self.pos] == 1:
            # hit obstacle
            self.dieSequence()
            return
        self.board[3][self.pos] = 2
        self.score += 1 


    def dieSequence(self):
        self.alive = False  # now dead
        self.board = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]


if __name__ == '__main__':
    # testing game, not important
    def renderboard():
        os.system('clear')
        for i in game.board:
            for j in i:
                print(j, end=' ')
            print('')

    game = Game()
    renderboard()
    while game.alive:
        time.sleep(0.5)
        game.moveright()
        game.advance()
        renderboard()


