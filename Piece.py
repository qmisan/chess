class Piece(object):
    """
    Docstring for piece class

    """
    types = {
            "KING"   : 0,
            "QUEEN"  : 1,
            "ROOK"   : 3,
            "BISHOP" : 4,
            "KNIGHT" : 5,
            "PAWN"   : 6
            }

    type = None
    owner = None

    def __init__(self, t, o):
        """
        @param t type of the piece
        @param o owner of the piece
        """
        self.type = t
        self.owner = o

    def __str__(self):
        return self.types[self.type]

    def getName(self):
        return self.type
        