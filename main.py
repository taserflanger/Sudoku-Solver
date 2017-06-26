from case import Case
from refs import *
from board import Board

example = [
    [8, 6, 2, 0, 4, 1, 0, 0, 0],
    [0, 0, 4, 0, 9, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 0, 1, 0, 8],
    [1, 4, 0, 9, 0, 0, 0, 3, 0],
    [0, 3, 8, 0, 0, 0, 0, 7, 0],
    [0, 7, 0, 0, 8, 4, 0, 0, 1],
    [7, 0, 6, 0, 0, 0, 0, 0, 5],
    [0, 0, 0, 8, 0, 0, 0, 0, 6],
    [5, 0, 0, 0, 1, 2, 7, 0, 4]
]
# setting up the grid

grid = []
for l in range(9):
    line = []
    for case in range(9):
        line.append(Case(l, case, 0))
    grid.append(line)


input_sudoku = open("sudoku.txt", "r", encoding="utf-8")
grid = textInput(input_sudoku)
# setGrid(example, grid)
board = Board(grid)
printGrid(grid)

board.solve()

input("End the progrmam")
