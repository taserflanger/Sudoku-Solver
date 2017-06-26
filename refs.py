from case import Case

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