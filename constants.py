import pygame
from math import sqrt


DEBUG = True


# Game Size
SIZE = 9
SQ = int(sqrt(SIZE))
REGIONS = [x for x in range(SIZE + 1) if x % SQ == 0]


# Console text
YES = {'Yes', 'yes', 'y', 'Y'}
OVERWRITE = """
>> There is a number already there.
>> Do you want to overwrite this cell? """
START = 'Click on a cell to begin'
TYPE = 'Type a number to place in highlighted cell'
YOUWIN = 'You win!'
BOARDINCOMPLETE = 'Board is not filled in completely!'
INCORRECT = 'Not a solution! Try again'


# Physical board space
WINDOW_SIZE = (500, 500)
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
TEXT_SPACE = 5
Y1 = 70
X1 = 70
SQUARE_SIZE = 40

# Verify Button
VBTN_LOC = (WINDOW_SIZE[0] // 6, 1.25 * Y1 + SQUARE_SIZE * SIZE)
VTXT_LOC = (WINDOW_SIZE[0] // 6 + 10, 1.3 * Y1 + SQUARE_SIZE * SIZE)

# Solve Button
SBTN_LOC = (WINDOW_SIZE[0] // 2, 1.25 * Y1 + SQUARE_SIZE * SIZE)
STXT_LOC = (WINDOW_SIZE[0] // 2 + 10, 1.3 * Y1 + SQUARE_SIZE * SIZE)


# Colors
GREY = ( 79,  93, 115)
BLACKCOLOR   = (  0,   0,   0)
WHITE        = (255, 255, 255)
BLUE         = (194, 255, 255)