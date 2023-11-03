import sys
import pygame
from Board import Board


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([400, 400])
        pygame.display.set_caption('Game')
        pygame.font.init()
        self.myfont30 = pygame.font.SysFont('Comic Sans MS', 30)
        self.myfont45 = pygame.font.SysFont('Comic Sans MS', 45)

    def draw(self, table):
        self.screen.fill((0, 0, 0))
        text = self.myfont45.render('Game', False, (128, 255, 0))
        self.screen.blit(text, (0, 0))
        for x in range(0, 4):
            for y in range(0, 4):
                text = self.myfont30.render(str(table[y][x].getVal()), False, (255, 255, 0))
                self.screen.blit(text, (x*100+20, y*75+100))
        pygame.display.flip()

    def run(self, board: Board):
        board.randomizeElement()
        while True:
            self.draw(board.getTable())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_UP:
                            if board.up():
                                board.randomizeElement()
                        case pygame.K_DOWN:
                            if board.down():
                                board.randomizeElement()
                        case pygame.K_LEFT:
                            if board.left():
                                board.randomizeElement()
                        case pygame.K_RIGHT:
                            if board.right():
                                board.randomizeElement()
                        case pygame.K_z:
                            for x in range(0, 4):
                                for y in range(0, 4):
                                    board.board[y][x].setVal(board.prevBoard[y][x].getVal())
                        case pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
