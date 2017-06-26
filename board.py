"""The board holds all version of the grid, from the first to the HEAD,
it goes recursively through the grid to solve the sudoku"""

from refs import *

class Board(object):
    def __init__(self, grid):
        self.grids = [grid]

    def iterate(self):
        grid = self.grids[-1]
        """Tries to find every case where the number
        can be set, so every case with 8 illegal
        numbers and 1 legal"""
        finished = True
        for line in grid:
            for case in line:
                if case.val == 0:
                    finished = False
                    #finding numbers in line
                    numbers_line = []
                    l = grid[case.line]
                    for c in l:
                        if c.val != 0:
                            numbers_line.append(c.val)

                    # finding numbers in box

                    numbers_box = []
                    for a in range(3):
                        for b in range(3):
                            c = (grid[case.line//3*3+a][case.col//3*3+b])
                            if c.val != 0:
                                numbers_box.append(c.val)

                    # finding numbers in col

                    numbers_col = []
                    for line in range(9):
                        c = grid[line][case.col]
                        if c.val != 0:
                            numbers_col.append(c.val)

                    [excepts] = [numbers_line + numbers_box + numbers_col]

                    for exc in excepts:
                        if exc not in case.excepts:
                            case.excepts.append(exc)

                    exc_len = len(case.excepts)

                    if exc_len == 8:
                        [number] = [i for i in range(1, 10) if i not in case.excepts]
                        case.val = number
                        printGrid(grid)
        return (finished, grid[:])