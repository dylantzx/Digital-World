import math

class Coordinate:

    def __init__(self, x=0,y=0): #self is always called during instantiation; it is a special method
        self.x= x 
        self.y= y #self.x and self.y creates an object instance
        
    def magnitude(self): #points to the object instance
        #return math.sqrt(self.x**2 + self.y**2)
        return math.hypot(self.x, self.y)
    
    def translate(self, dx, dy):
        self.x+=dx
        self.y+=dy
        return (dx, dy)
    
    def __eq__(self, other): #allows you to do print(p==q)
        return self.x == other.x and self.y == other.y
    
p = Coordinate()
print(p.x, p.y)
print(p.magnitude()) #p alr has x and y so no need to put it as parameters
p.x = 3
p.y = 4
print(p.magnitude()) #converted to Coordinate.magnitude(p) therefore 1 argument
q= Coordinate(3,4) #After init, init frame destroyed
print(p == q) # p is self, q is other
q.translate(1,2)
print(q.x)
print(p==q)
