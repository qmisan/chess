class Coordinate(object):
    """
    docstring for Coordinate class
    """

    # Coordinate fields
    POSSIBLE_X = [0, 1, 2, 3, 4, 5, 6, 7, None]
    POSSIBLE_Y = ["a", "b", "c", "d", "e", "f", "g", "h", None]

class Coordinates(Object):
    x = None
    y = None

    def __init__(self, x , y):
        if x not in POSSIBLE_X or y not in POSSIBLE_Y:
            Logger("Not valid coordinate")
        else:
            self.x = x
            self.y = y
