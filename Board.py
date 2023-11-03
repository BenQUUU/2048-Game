from random import randint
from Element import Element


class Board:
    def __init__(self):
        self.board = [[], [], [], []]
        self.prevBoard = [[], [], [], []]
        for x in range(0, 4):
            for y in range(0, 4):
                self.board[y].append(Element())
                self.prevBoard[y].append(Element())

    def randomizeElement(self):
        #Randomizing a new element
        x = randint(0, 3)
        y = randint(0, 3)

        while self.board[y][x].getVal() != 0:
            x = randint(0, 3)
            y = randint(0, 3)

        self.board[y][x].setVal(randint(1, 2) * 2)
