from square import Square

class Board(object):
    """
    Board consists of 8x8 field of squares.
    squares are indicaded with coordinates from a to
    """
    squares = []
    def __init__(self):
        for x in range(8):
            for y in range(8):
                self.squares.Add(Square(x,y))

