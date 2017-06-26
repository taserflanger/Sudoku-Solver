"""Case Module, each case of the grid is going to be self object"""
class Case(object):
    """Case Object"""
    def __init__(self, line, column, val):
        self.line = line
        self.col = column
        self.val = val
        self.excepts = []
    
    def __repr__(self):
        return str(self.val)+" (%s, %s)"% (self.line, self.col)
        