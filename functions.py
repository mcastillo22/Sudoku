import pygame
from constants import *


# Setup board visuals

def setup_board():
    SCREEN.fill(WHITE)
    draw_grid()
    show_button('Verify Puzzle', VBTN_LOC, VTXT_LOC)
    show_button('Solve Puzzle', SBTN_LOC, STXT_LOC)

def highlight(pos, color):
    square = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
    square.set_alpha(64)
    square.fill(color)
    SCREEN.blit(square, (pos))

def place_numbers(board, given_spaces):
    txt_obj = pygame.font.SysFont('Calibri', 28)
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] is None:
                continue
            number = txt_obj.render(str(board[row][col]), True, BLACKCOLOR)

            # Place given numbers with a grey backgroung
            if not can_write(row, col, given_spaces):
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

def show_message(message):
    txt_obj = pygame.font.SysFont('Calibri', 24)
    turn = txt_obj.render(message, True, BLACKCOLOR)
    SCREEN.blit(turn, (X1 // 2, Y1 // 3))

def show_button(message, btn_loc, txt_loc):
    txt_obj = pygame.font.SysFont('Calibri', 24)
    text = txt_obj.render(message, True, BLACKCOLOR)

    btn = pygame.Surface((4*SQUARE_SIZE, SQUARE_SIZE))
    btn.fill(BLUE)

    SCREEN.blit(btn, btn_loc)
    SCREEN.blit(text, txt_loc)


# Validate user clicks on grid

def validate_click(mouse_click, given_spaces):
    mouse_y, mouse_x = mouse_click

    coord_x, coord_y = on_grid(mouse_x, mouse_y)
    in_board = coord_x is not None and coord_y is not None

    if in_board and can_write(coord_x, coord_y, given_spaces):
        if DEBUG:
            print(coord_x, coord_y)
        return (coord_x, coord_y)

    return False

def can_write(x, y, given_spaces):
    try:
        if y in given_spaces[x]:
            return False
    except:
        return True
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


# Validate user typing

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
        if key == 8:
            game.set(None, cell)
            return True
        
        print('Type a number!')
        return False
    
    return True

# Verify buttons

def validate_button(location, game):
    verify = pygame.Rect(VBTN_LOC[0], VBTN_LOC[1], BTN_SIZE[0], BTN_SIZE[1])
    solve = pygame.Rect(SBTN_LOC[0], SBTN_LOC[1], BTN_SIZE[0], BTN_SIZE[1])

    if verify.collidepoint(location):
        print('Verifying')
        return str(game.verify())
    if solve.collidepoint(location):
        print('Solving')
        return str(game.solve())

    return None