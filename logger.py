import time

filepath = "log.txt"
f = open(filepath,"a")

def timestamp():
    return "[" + str(time.time()) + "]"
    
def StartLine(string):
    temp_string = timestamp() + "\t" + string
    f.write(temp_string)

def ContinueLine(string):
    f.write(string)

def EndLine(string):
    f.write(string + "\n")

def WriteLine(string):
    f.write(timestamp() + "\t" + string + "\n")
        