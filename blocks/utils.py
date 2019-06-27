#Utils for fixing shit
import random
from cell import Cell
import consts as consts

def rand_color():
    cyan = (0, 255, 255)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    pink = (255, 100, 255)
    COLORS = [cyan, yellow, red, green, blue, pink]
    return random.choice(COLORS)

def generate_board():
    list = []
    x = 0
    y = 0
    for i in range(0, consts.BOARD_SIZE):
        for j in range(0, consts.BOARD_SIZE):
            list.append(Cell(x, y, rand_color(), False, None, None, None, None))
            x += consts.CELL_SIZE
        x = 0
        y += consts.CELL_SIZE
    fix_links(list, consts.BOARD_SIZE)
    return list

def fix_links(arr, board_size):
    counter = 0
    for i in range(len(arr)):        
        if counter == 0:
            arr[i].right = arr[i+1]
            counter += 1
        
            if i - consts.BOARD_SIZE >= 0:
                arr[i].top = arr[i-consts.BOARD_SIZE]

            if i - (consts.BOARD_SIZE * consts.BOARD_SIZE - consts.BOARD_SIZE) < 0:
                arr[i].bottom = arr[i + consts.BOARD_SIZE]
        elif counter == consts.BOARD_SIZE - 1:
            arr[i].left = arr[i-1]
            counter = 0

            if i - consts.BOARD_SIZE >= 0:
                arr[i].top = arr[i - consts.BOARD_SIZE]

            if i - (consts.BOARD_SIZE * consts.BOARD_SIZE - consts.BOARD_SIZE) < 0:
                arr[i].bottom = arr[i + consts.BOARD_SIZE]
        else:
            arr[i].right = arr[i+1]
            arr[i].left = arr[i-1]
            counter +=1

            if i - consts.BOARD_SIZE >= 0:
                arr[i].top = arr[i-consts.BOARD_SIZE]

            if i - (consts.BOARD_SIZE * consts.BOARD_SIZE - consts.BOARD_SIZE) < 0:
                arr[i].bottom = arr[i + consts.BOARD_SIZE]
