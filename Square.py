class Square(object):
    """
    Docstring for board class
    """
    piece = None

    def __init__(self, x, y):
    	self.coords = tuple(x, y)

    def set_piece(self, piece):
    	self.piece = piece

    def remove_piece(self, piece):
    	self.piece = None