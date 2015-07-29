class Piece(object):
    """
    Docstring for piece class

    """
    types = {
            "KING" : 0
            "QUEEN" : 1
            "ROOK" : 3
            "BISHOP" : 4
            "KNIGHT" : 5
            "PAWN" : 6
            }

    self.type = None

    def __init__(self, type):
        self.type = type

    def __str__(self):
        return self.types[self.type]

    def getName(self):
        return self.type
        