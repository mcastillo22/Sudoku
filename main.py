import pygame, sys
from pygame.locals import  * 
from Sudoku import Sudoku
from constants import *
from setup import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Sudoku')

    new_game = Sudoku(SIZE)
    cell = False
    message = None
    running = True

    while running:
        clock.tick(60)
        setup_board()
        place_numbers(new_game.get_board(), new_game.get_hardcode())
        show_text(message)

        if cell is not False:
            highlight(convert_to_screen(cell), BLUE)
            show_text(message)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                continue

            if event.type == pygame.MOUSEBUTTONDOWN:
                location = event.pos
                if event.button == 1:
                    cell = validate_click(location,
                            new_game.get_hardcode())
                    if not cell:
                        if validate_button(location):
                            message = new_game.verify()
                        else:
                            message = None
                    else:
                        message = TYPE

            if cell:
                if event.type == pygame.KEYDOWN:
                    if validate_type(event.key, new_game, cell):
                        cell = False

        pygame.display.update()
    
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
