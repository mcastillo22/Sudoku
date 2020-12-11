from constants import *


from math import sqrt
from random import randint


class Sudoku:
    """A Sudoku Game"""
    def __init__(self, size):
        self._game_state = "UNFINISHED"
        self._board = SudokuBoard(size)
        self._CLI = False

    def set_CLI(self):
        self._CLI = True

    def is_complete(self):
        """Determines if board is complete"""
        return self._board.is_complete()

    def verify(self):
        """Verifies if the current puzzes is a solution"""
        if not self._board.is_complete():
            print('\n\033[0;31mBoard is not filled in!\033[0m')
            return 'Board is not filled in completely'
        solution = self._board.verify()
        if solution:
            print('You win!')
            return 'You win!'
        else:
            print('\033[0;31mNot a solution try again!\033[0m\n')
            return 'Not a solution! Try again'

    def print(self):
        """Prints board to terminal"""
        if self._CLI or DEBUG:
            self._board.print()

    def convert_coord(self, position):
        """Converts from AlphaNumeric to lists of lists"""
        alpha = 'ABCDEFGHI'
        row = position[1] - 1
        col = alpha.index(position[0].upper())
        return (row, col)

    def set(self, number, position):
        """Sets number to board"""
        if self._CLI:
            position = self.convert_coord(position)
        if DEBUG or self._CLI is False:
            self._board.set(number, position)
            return True
        else:
            if self._board.cell_is_empty(position):
                self._board.set(number, position)
                return True
            else:
                check_overwrite = input(OVERWRITE)
                if check_overwrite in YES:
                    self._board.set(number, position)
                    return True
                else:
                    return False

    def complete(self):
        """Fills in board"""
        self._board.initiate_complete()

    def random_fill(self):
        """Randomly fills in board"""
        self._board.random_fill()
    
    def reset(self):
        """Resets to initial puzzle"""
        self._board.initiate_new()

    def get_board(self):
        return self._board.return_board()

    def get_hardcode(self):
        return self._board.get_hardcode()

class SudokuBoard:
    """Sudoku Board of a Sudoku Game"""
    def __init__(self, size):
        self._size = size
        self._square = int(sqrt(size))
        # self._board = \
        #     [[None for x in range(size)] for y in range(size)]
        self._square_size = self._size * 4 + 4
        self.initiate_new()
        self._hardcode = self.no_overwrite()
    
    def get_hardcode(self):
        """Returns dictionary of spaces that cannot be overwritten"""
        return self._hardcode

    def no_overwrite(self):
        """Determines which cells cannot be overwritten"""
        results = {}
        for row in range(SIZE):
            results[row] = set()
            for col in range(SIZE):
                if self._board[row][col] is not None:
                    results[row].add(col)
        return results

    def print(self):
        """Prints board to terminal"""
        def print_horizontal():
            print('\033[1;34m╠\033[0m' +
                '\033[1;34m═\033[0m' * (self._square_size - 5) +
                '\033[1;34m╣\033[0m')
        
        def print_alpha():
            alpha = 'ABCDEFGHI'
            print(' ', end='')
            for a in alpha:
                print(f' {a} ', end=' ')
            print()

        row_count = 0
        print_alpha()
        print_horizontal()
        for row in self._board:
            col_count = 0
            row_count += 1
            print('\033[1;34m║\033[0m', end='')

            for col in row:
                col_count += 1
                if col is None:
                    col = ' '
                if col_count % self._square == 0:
                    print(f' {col} ', end='\033[1;34m║\033[0m')
                else:
                    print(f' {col} ', end='\033[1;34m│\033[0m')
            print(f' {row_count}')

            if row_count % self._square == 0:
                print_horizontal()

    def initiate_new(self):
        """Create new puzzle"""
        self._board = [[9, 4, 8, 6, None, None, 3, None, 1],
            [None, None, 5, 8, None, None, 4, 6, 9],
            [6, None, None, 5, 4, None, 2, None, None],
            [3, None, 7, 4, 1, 5, 6, 9, None],
            [None, None, None, None, 6, 3, 8, None, None],
            [None, 1, None, 9, 2, None, None, None, 4],
            [None, None, None, 3, 9, None, None, None, 8],
            [None, 2, None, None, 5, 7, None, None, None],
            [1, None, None, 2, None, 4, None, None, None]]

    def initiate_complete(self):
        """For testing purposes. Fills in the entire board"""
        self._board = [[9, 4, 8, 6, 7, 2, 3, 5, 1],
            [2, 7, 5, 8, 3, 1, 4, 6, 9],
            [6, 3, 1, 5, 4, 9, 2, 8, 7],
            [3, 8, 7, 4, 1, 5, 6, 9, 2],
            [4, 9, 2, 7, 6, 3, 8, 1, 5],
            [5, 1, 6, 9, 2, 8, 7, 3, 4],
            [7, 5, 4, 3, 9, 6, 1, 2, 8],
            [8, 2, 3, 1, 5, 7, 9, 4, 6],
            [1, 6, 9, 2, 8, 4, 5, 7, 3]]  

    def random_fill(self):
        """Randomly fills in empty squares"""
        for row in range(self._size):
            for col in range(self._size):
                if self._board[row][col] is None:
                    self._board[row][col] = randint(1,9)

    def is_complete(self):
        """Checks if board has been filled out"""
        for row in self._board:
            for col in row:
                if col is None:
                    return False
        return True

    def cell_is_empty(self, position):
        """Determines if the cell at the passed position is empty or not"""
        x = position[0]
        y = position[1]
        if self._board[x][y] is None:
            return True
        return False

    def set(self, number, position):
        """Sets the give number in the given position on the board"""
        x, y = position

        self._board[x][y] = number

    def verify(self):
        """Verifies if the user solution is correct"""
        return self.verify_row() and self.verify_col() \
            and self.verify_square()

    def verify_row(self):
        """Checks current puzzle is a proper solution for all rows"""        
        for row in self._board:
            col_set = set()
            for col in row:
                if col in col_set:
                    return False
                col_set.add(col)
        
        return True

    def verify_col(self):
        """Verifies current puzzle is a solution for all columns"""
        for y in range(self._size):
            col_set = set()
            for x in range(self._size):
                if self._board[x][y] in col_set:
                    return False
                col_set.add(self._board[x][y])
        
        return True
    
    def verify_square(self):
        """Verifies current puzzle is a solution for all squares"""
        sq_positions = [0] + \
            [x for x in range(2, self._size) if \
                x % self._square == 0]
        if DEBUG:
            print(sq_positions)
        for spr in sq_positions:
            for spc in sq_positions:
                sq = set()
                for row in range(self._square):
                    for col in range(self._square):
                        sq.add(self._board[spr + row][spc + col])
                if DEBUG:
                    print(self._board[spr][spc], ':', sq)
                if len(sq) != self._size:
                    return False
        return True

    def return_board(self):
        return self._board