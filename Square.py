class Square(object):
    """
    Docstring for board class

    """
    piece = None
    column = None
    row = None

    def __init__(self, x, y):
        self.column = x
        self.row = y

    def __str__(self):
        if self.piece != None:
            return str(self.piece)
        else:
            return "."
            
    def set_piece(self, piece):
        self.piece = piece

    def remove_piece(self, piece):
        self.piece = None

    