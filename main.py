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
board = Board(grid)
finished = board.iterate()[0]
printGrid(grid)

i = 0
while (not finished) and (i < 1000):
    
    finished, grid = board.iterate()
    if finished:
        pass
    
    i += 1
    printGrid(grid)
    if (not finished) and (i >= 999):
        print("Unsolvable for this programm")
input("End the progrmam")
