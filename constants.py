import pygame
from math import sqrt


DEBUG = True


# Game Size
SIZE = 9
SQ = int(sqrt(SIZE))

# Console text
YES = {'Yes', 'yes', 'y', 'Y'}
OVERWRITE = """
>> There is a number already there.
>> Do you want to overwrite this cell? """


# Physical board space
WINDOW_SIZE = (500, 500)
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
TEXT_SPACE = 5
Y1 = 70
X1 = 70
SQUARE_SIZE = 40


# Colors
SLEET = ( 79,  93, 115)
BLACKCOLOR   = (  0,   0,   0)
WHITE        = (255, 255, 255)
BLUE         = (194, 255, 255)