import pygame


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