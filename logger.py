import time

class Logger(object):
    def __init__(self, filepath):
        f = open(filepath, "w")
        
    def Info(string):
        timestamp = "[" + time() + "]"
        f.write(timestamp + "\t" + string + '\n')
        if debug_mode = True
            print(string)