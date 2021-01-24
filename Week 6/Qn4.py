import math
import sys

class Coordinate():
    x=0
    y=0

def get_magnitude(x,y):
    return math.sqrt(math.pow(x,2)+math.pow(y,2))

def get_maxmin_mag(f):
    maxsofar = -1
    minsofar = sys.maxsize
    pmax = Coordinate()
    pmin = Coordinate()
    for line in f:
        data = line.split()
        x,y = float(data[0].strip()),float(data[1].strip())
        mag = get_magnitude(x,y)
        if mag > maxsofar:
            maxsofar = mag
            pmax.x = x
            pmax.y = y
        if mag < minsofar:
            minsofar = mag
            pmin.x = x
            pmin.y = y
    return pmax, pmin
fo = open('xy.dat','r') #r for reading, a for append, w for writing
maxcoord, mincoord = get_maxmin_mag(fo)

print("max: ({:f},{:f})".format(maxcoord.x, maxcoord.y))
print("min: ({:f},{:f})".format(mincoord.x, mincoord.y))
fo.close()

    
