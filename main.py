from Board import Board
import logging

if __name__ == "__main__":
    LOG_FILENAME = 'debug.log'
    logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
    
    b = Board()
    b.print_to_console()