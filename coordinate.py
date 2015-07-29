import Logger
from Errors import BadValueError

# Coordinate fields
POSSIBLE_X = [0, 1, 2, 3, 4, 5, 6, 7, None]
POSSIBLE_Y = ["a", "b", "c", "d", "e", "f", "g", "h", None]

class Coordinate(object):
    """
    docstring for Coordinate class
    """

    x = None
    y = None

    def __init__(self, x , y):

        if (x not in POSSIBLE_X):
            Logger.WriteLine("{0} is not valid coordinate in X-direction".format(x))
            raise BadValueError("Wrong coordinate data")

        if (y not in POSSIBLE_Y):
            Logger.WriteLine("{0} is not valid coordinate in Y-direction".format(y))
            raise BadValueError("Wrong coordinate data")

        else:
            self.x = x
            self.y = y

    def intToChar(self, integer):
        index = POSSIBLE_X.index(integer)
        return POSSIBLE_Y[index]

    def charToInt(self, character):
        index = POSSIBLE_Y.index(integer)
        return POSSIBLE_[Xindex]