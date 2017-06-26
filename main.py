from case import Case

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

def textInput(text):
    g = []
    for x in range(9):
        l = text.readline()
        line = []
        y = -1
        for char in l:
            y += 1
            if char != "\n":
                line.append(Case(x, y, int(char)))
        g.append(line)
    return g

def setGrid(setup, target):
    """Transforms an empty grid into 
    an example or a user entry"""

    for line in range(9):
        for case in range(9):
            value = setup[line][case]
            target[line][case].val = value

# setting up the grid

grid = []
for l in range(9):
    line = []
    for case in range(9):
        line.append(Case(l, case, 0))
    grid.append(line)

def printGrid(grid):
    """function to print out the grid"""
    res = ""
    #iterating through and finding every 3 case in each direction
    for b_line in range(3):
        res+="\n"
        for line in range(3):
            res+="\n"
            for col in range(3):
                res+="  "
                for case in range(3):
                    value = grid[3*b_line+line][3*col+case]
                    res += str(value.val) + " "
    print(res, "\n")
    return res

def iterate(grid):
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

input_sudoku = open("sudoku2.txt", "r", encoding="utf-8")
grid = textInput(input_sudoku)
finished = iterate(grid)[0]
printGrid(grid)
i = 0


while (not finished) and (i < 1000):
    
    finished, grid = iterate(grid)
    if finished:
        pass
    
    i += 1
    printGrid(grid)
    if (not finished) and (i >= 999):
        print("Unsolvable for this programm")
input("End the progrmam")