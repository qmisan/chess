from Square import Square
import logging

class Board(object):
    """
    Board consists of 64 squares.
    squares are indicaded with number from 0 to 63 from a to

                0  1  2  3  4  5  6  7
                8  9  10 11 12 13 14 15
                16 17 18 19 20 21 22 23
                24 25 26 27 28 29 30 31
                32 33 34 35 36 37 38 39
                40 41 42 43 44 45 46 47
                48 49 50 51 52 53 54 55
                56 57 58 59 60 61 62 63

    Its easy to indicate what column and row squares are in
    """

    squares = list()

    def __init__(self):
        # Initializes board which is 8x8 table of squares
        logging.debug("Initializing squares...")

        for index in range(64):
            self.squares.append(Square(int(index/8), index % 8))
        logging.debug("done!")

    def print_to_console(self):
        string = ""
        for i in range(len(self.squares)):
            if(i % 8 == 0 and i != 0):
                string += "\n"
            string += str(self.squares[i])
        print(string)