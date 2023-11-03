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

    def getTable(self):
        return self.board

    def copyTable(self):
        for x in range(0, 4):
            for y in range(0, 4):
                self.prevBoard[y][x].setVal(self.board[y][x].getVal())

    def right(self) -> bool:
        self.copyTable()
        for z in range(0, 3):
            for x in range(0, 3):
                for y in range(0, 4):
                    x = 2-x
                    if self.board[y][x+1].getVal() == 0:
                        self.board[y][x+1].setVal(self.board[y][x].getVal())
                        self.board[y][x].delVal()
                    elif self.board[y][x].getVal() == self.board[y][x+1].getVal():
                        self.board[y][x+1].setVal(self.board[y][x].getVal() * 2)
                        self.board[y][x].delVal()

        for x in range(0, 4):
            for y in range(0, 4):
                if self.prevBoard[y][x].getVal() != self.board[y][x].getVal():
                    return True

        return False

    def left(self) -> bool:
        self.copyTable()
        for z in range(0, 3):
            for x in range(1, 4):
                for y in range(0, 4):
                    if self.board[y][x-1].getVal() == 0:
                        self.board[y][x-1].setVal(self.board[y][x].getVal())
                        self.board[y][x].delVal()
                    elif self.board[y][x].getVal() == self.board[y][x-1].getVal():
                        self.board[y][x-1].setVal(self.board[y][x].getVal() * 2)
                        self.board[y][x].delVal()

        for x in range(0, 4):
            for y in range(0, 4):
                if self.prevBoard[y][x].getVal() != self.board[y][x].getVal():
                    return True

        return False

    def up(self) -> bool:
        self.copyTable()
        for z in range(0, 3):
            for x in range(0, 4):
                for y in range(1, 4):
                    if self.board[y-1][x].getVal() == 0:
                        self.board[y-1][x].setVal(self.board[y][x].getVal())
                        self.board[y][x].delVal()
                    elif self.board[y][x].getVal() == self.board[y-1][x].getVal():
                        self.board[y-1][x].setVal(self.board[y][x].getVal() * 2)
                        self.board[y][x].delVal()

        for x in range(0, 4):
            for y in range(0, 4):
                if self.prevBoard[y][x].getVal() != self.board[y][x].getVal():
                    return True

        return False

    def down(self) -> bool:
        self.copyTable()
        for z in range(0, 3):
            for x in range(0, 4):
                for y in range(0, 3):
                    y = 2 - y
                    if self.board[y+1][x].getVal() == 0:
                        self.board[y+1][x].setVal(self.board[y][x].getVal())
                        self.board[y][x].delVal()
                    elif self.board[y][x].getVal() == self.board[y+1][x].getVal():
                        self.board[y+1][x].setVal(self.board[y][x].getVal() * 2)
                        self.board[y][x].delVal()

        for x in range(0, 4):
            for y in range(0, 4):
                if self.prevBoard[y][x].getVal() != self.board[y][x].getVal():
                    return True

        return False
