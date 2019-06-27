import pygame
import consts


class Cell:
    def __init__(self, x, y, color, flooded, left=None, top=None, right=None, bottom=None):
        self.x = x
        self.y = y
        self.color = color
        self.flooded = flooded
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    def draw(self):
        pygame.draw.rect(consts.GAME_DISPLAY,
                         self.color, (self.x, self.y, consts.CELL_SIZE, consts.CELL_SIZE))
        #x, y, width, height
