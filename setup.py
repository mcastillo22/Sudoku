import pygame
from constants import *


# setup board

def setup_board():
    SCREEN.fill(WHITE)
    draw_grid()
    show_button()

def highlight(pos, color):
    square = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
    square.set_alpha(64)
    square.fill(color)
    SCREEN.blit(square, (pos))

def place_numbers(board, hard_spaces):
    txt_obj = pygame.font.SysFont('Calibri', 28)
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] is None:
                continue
            number = txt_obj.render(str(board[row][col]), True, BLACKCOLOR)

            if not can_write(row, col, hard_spaces):
                highlight((X1 + col * SQUARE_SIZE, Y1 + row * SQUARE_SIZE), GREY)
            
            SCREEN.blit(number, (2.5 * TEXT_SPACE + X1 + SQUARE_SIZE * col,
                TEXT_SPACE + Y1 + SQUARE_SIZE * row))

def draw_grid():
    for n in range(Y1, Y1 + SIZE * SQUARE_SIZE + 1, SQUARE_SIZE):
        if (n - Y1) % SQ == 0:
            pygame.draw.line(SCREEN, BLACKCOLOR, (X1, n),
                (X1 + SQUARE_SIZE * SIZE, n), SQ)
            pygame.draw.line(SCREEN, BLACKCOLOR, (n, Y1),
                (n, Y1 + SQUARE_SIZE * SIZE), SQ)
        pygame.draw.line(SCREEN, BLACKCOLOR, (X1, n),
            (X1 + SQUARE_SIZE * SIZE, n), 1)
        pygame.draw.line(SCREEN, BLACKCOLOR, (n, Y1),
            (n, Y1 + SQUARE_SIZE * SIZE), 1)

def show_text(phrase):
    txt_obj = pygame.font.SysFont('Calibri', 24)
    turn = txt_obj.render(phrase, True, BLACKCOLOR)
    SCREEN.blit(turn, (X1 // 2, Y1 // 3))

def show_button():
    txt_obj = pygame.font.SysFont('Calibri', 24)
    verify = txt_obj.render('Verify Puzzle', True, BLACKCOLOR)

    btn = pygame.Surface((4*SQUARE_SIZE, SQUARE_SIZE))
    btn.fill(BLUE)

    SCREEN.blit(btn, (WINDOW_SIZE[0] // 3, 1.25 * Y1 + SQUARE_SIZE * SIZE))
    SCREEN.blit(verify, (WINDOW_SIZE[0] // 3 + 10, 1.3 * Y1 + SQUARE_SIZE * SIZE))


# validate click

def validate_click(mouse_click, hard_spaces):
    mouse_y, mouse_x = mouse_click

    coord_x, coord_y = on_grid(mouse_x, mouse_y)
    in_board = coord_x is not None and coord_y is not None

    if in_board and can_write(coord_x, coord_y, hard_spaces):
        if DEBUG:
            print(coord_x, coord_y)
        return (coord_x, coord_y)

    return False

def can_write(x, y, hard_spaces):
    if y in hard_spaces[x]:
        return False
    return True

def on_grid(x, y):
    for x1 in range(X1, (SIZE + 1) * SQUARE_SIZE, SQUARE_SIZE):
        for y1 in range(Y1, (SIZE + 1) * SQUARE_SIZE, SQUARE_SIZE):
            box = pygame.Rect(x1, y1, SQUARE_SIZE, SQUARE_SIZE)
            if box.collidepoint(x, y):
                return convert_to_array((x1, y1))

    return (None, None)

def convert_to_array(pos):
    x, y = pos
    return int((x - X1) / SQUARE_SIZE), int((y - Y1) / SQUARE_SIZE)

def convert_to_screen(pos):
    y, x = pos
    return (X1 + x * SQUARE_SIZE, Y1 + y * SQUARE_SIZE)


# validate type

def validate_type(key, game, cell):
    try:
        number = int(chr(key))
        if number in set([x for x in range(1, SIZE + 1)]):
            try:
                game.set(number, cell)
            except:
                print("Try again!")
                return False
    
    except:
        print('Type a number!')
        return False
    
    return True

# Verify button click

def validate_button(location):
    box = pygame.Rect(WINDOW_SIZE[0] // 3, 1.25 * Y1 + SQUARE_SIZE * SIZE,
        4 * SQUARE_SIZE, SQUARE_SIZE)
    if box.collidepoint(location):
        print('Verifying')
        return True    
    return False