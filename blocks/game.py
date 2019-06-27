import pygame
import time
import random
import utils as utils
from cell import Cell
import consts as consts

board = utils.generate_board()

pygame.init()

# Global variables are bad lol
display_width = consts.DISPLAY_WIDTH
display_height = consts.DISPLAY_HEIGHT
black = (0,0,0)
white = (255,255,255)
done = False

pygame.display.set_caption('FloodIt Game!')
clock = pygame.time.Clock()

# draws the entire board
def draw_board():
        for cell in board:                
                cell.draw()

# GAME LOOP
def game_loop(done):    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        consts.GAME_DISPLAY.fill(white)  
        draw_board()        
        pygame.display.update()
        clock.tick(60)

game_loop(done)
pygame.quit()