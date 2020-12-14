from constants import *


from math import sqrt
from random import randint


class Sudoku:
    """A Sudoku Game"""
    def __init__(self, size):
        self._game_state = "UNFINISHED"
        self._board = SudokuBoard()
        self._CLI = False

    def set_CLI(self):
        """Sets CLI play to True"""
        self._CLI = True

    def verify(self):
        """Verifies if the current puzzes is a solution"""
        if not self._board.is_complete():
            print('\n\033[0;31m' + BOARDINCOMPLETE + '\033[0m')
            return BOARDINCOMPLETE
        solution = self._board.verify()
        if solution:
            print(YOUWIN)
            return YOUWIN
        else:
            print('\033[0;31m' + INCORRECT + '\033[0m\n')
            return INCORRECT

    def print(self):
        """Prints board to terminal"""
        if self._CLI or DEBUG:
            self._board.print()

    def convert_coord(self, position):
        """For CLI. Converts from AlphaNumeric to lists of lists"""
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
            if self._board.is_cell_empty(position):
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

    def get_hard_cells(self):
        return self._board.get_hard_cells()

    def is_complete(self):
        """Determines if board is complete"""
        return self._board.is_complete()


class SudokuBoard:
    """Sudoku Board of a Sudoku Game"""
    def __init__(self):
        self._size = SIZE
        self._square = SQ
        # self._board = \
        #     [[None for x in range(size)] for y in range(size)]
        self.initiate_new()
        self._hard_cells = self.no_overwrite()
    
    def get_hard_cells(self):
        """Returns dictionary of spaces that cannot be overwritten"""
        return self._hard_cells

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
        square_size = self._size * 4 + 4
        def print_horizontal():
            print('\033[1;34m╠\033[0m' +
                '\033[1;34m═\033[0m' * (square_size - 5) +
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

    def is_cell_empty(self, position):
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
            and self.verify_region()

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
    
    def verify_region(self):
        """Verifies current puzzle is a solution for all squares"""
        sq_positions = [0] + \
            [x for x in range(2, self._size) if x % self._square == 0]
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


class SudokuGraph:
    """Graph representing the Sudoku Board"""
    def __init__(self):
        self._regions = [x for x in range(SIZE + 1) if x % SQ == 0]
        self._all = {}
        self.connect()

    def connect(self):
        """Creates the graph as a dictionary"""
        for x in range(SIZE):
            for y in range(SIZE):
                adjacent = self.connect_row((x,y))
                adjacent = adjacent.union(self.connect_col((x,y)))
                adjacent = adjacent.union(self.connect_region((x,y)))
                self._all[(x,y)] = adjacent
 
    def connect_col(self, node):
        """Connects all nodes in a column"""
        col = node[0]
        connect = set()
        for row in range(SIZE):
            if (row, col) != node:
                connect.add((row,col))
        return connect

    def connect_row(self, node):
        """Connects all nodes in a row"""
        row = node[0]
        connect = set()
        for col in range(SIZE):
            if (row, col) != node:
                connect.add((row,col))
        return connect

    def connect_region(self, node):
        """Connects the nodes in a region"""
        connect = set()
        region_x, region_y = -5, -5

        for x in range(SQ):
            if node[0] < self._regions[x]:
                region_x = self._regions[x-1]
                break

        for y in range(SQ):
            if node[1] < self._regions[y]:
                region_y = self._regions[y-1]
                break

        for row in range(SQ):
            for col in range(SQ):
                if (region_x + row,region_y + col) != node:
                    connect.add((region_x + row,region_y + col))
        
        return connect


tro = SudokuGraph()
print()
