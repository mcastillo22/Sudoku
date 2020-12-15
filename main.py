import pygame, sys
from pygame.locals import  * 
from Sudoku import Sudoku
from constants import *
from functions import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Sudoku')

    new_game = Sudoku(SIZE)
    cell = False
    message = START
    running = True

    while running:
        clock.tick(60)
        setup_board()
        place_numbers(new_game.get_board(), new_game.get_given())
        show_message(message)

        if cell is not False:
            highlight(convert_to_screen(cell), BLUE)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                continue

            if event.type == pygame.MOUSEBUTTONDOWN:
                location = event.pos
                if event.button == 1:
                    cell = validate_click(location,
                            new_game.get_given())
                    if not cell:
                        message = validate_button(location, new_game)
                    else:
                        message = TYPE

            if cell:
                if event.type == pygame.KEYDOWN:
                    if validate_type(event.key, new_game, cell):
                        cell = False
                        message = None

        pygame.display.update()
    
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
