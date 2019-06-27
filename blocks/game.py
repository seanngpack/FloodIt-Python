import pygame
import time
import random
import utils as utils
from cell import Cell
import consts as consts


class Game():

    def __init__(self, board, flooded=None, to_flood=None, current_color=None):
        self.board = board
        self.flooded = [self.board[0]]
        self.to_flood = [self.board[0]]
        self.current_color = self.board[0].color

    # global vars
    done = False
    pygame.display.set_caption('FloodIt Game!')
    clock = pygame.time.Clock()

    pygame.init()

    # draws the entire board
    def draw_board(self):
        for cell in self.board:
            cell.draw()

    # finds the color square the player clicked on
    def find_color(self, pos):
        for cell in self.board:
            left = cell.x
            right = cell.x + consts.CELL_SIZE
            top = cell.y
            bot = cell.y + consts.CELL_SIZE
            if pos[0] >= left and pos[0] <= right and pos[1] >= top and pos[1] <= bot:                                
                return cell.color
        return self.current_color

    # enables the flooded animation to happen
    def update_flooded(self):
        toFloodLater = []

        for cell in self.to_flood:
            neighbors = [cell.top, cell.bottom, cell.left, cell.right]

            for cell2 in neighbors:
                if cell2 != None:
                    if not cell2.flooded and cell2.color == self.current_color and not (cell2 in toFloodLater):
                        print('adding ' + str(cell.x) + ' ' + str(cell.y))
                        toFloodLater.append(cell2)
                    elif cell2.flooded and not cell2.color == self.current_color and not (cell2 in toFloodLater):
                        print('adding ' + str(cell.x) + ' ' + str(cell.y))
                        toFloodLater.append(cell2)

        for cell in self.to_flood:
            self.flooded.append(cell)
            self.draw_flooded(cell)
            print('drawing ' + str(cell.x) + ' ' + str(cell.y))

        self.to_flood = toFloodLater
        self.draw_board()

    # draws the flooded cells
    def draw_flooded(self, cell):
        cell.color = self.current_color
        cell.flooded = True
        cell.draw()

    # GAME LOOP
    def game_loop(self, done):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

                #consts.GAME_DISPLAY.fill((255, 255, 255))
                
                # self.draw_board()

                if event.type == pygame.MOUSEBUTTONUP:
                    if len(self.to_flood) == 0:
                        pos = pygame.mouse.get_pos()
                        self.current_color = self.find_color(pos)
                        self.to_flood = [self.board[0]]
                self.update_flooded()

                pygame.display.update()
                self.clock.tick(10)


board = utils.generate_board()
game1 = Game(board)
game1.game_loop(False)
pygame.quit()
