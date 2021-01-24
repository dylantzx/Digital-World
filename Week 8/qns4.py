class Line:

    def __init__(self, c_0, c_1):
        self._c0 = c_0
        self._c1 = c_1

    def __call__(self , x):
        y = self._c0 + self._c1*x
        return y

    def table(self, L, R, n):
        incre = (R-L)/(n-1)
        output = ""
        if n!=0:
            for times in range(n):
                y = self.__call__(L)
                out = "{:>10.2f}{:>10.2f}".format(L,y)
                output+=out
                output+="\n"
                if R>L:
                    L+=incre
                else:
                    break
            
        else:
            out="Error in printing table"
            output+=out
            
        return output
    
line = Line(1,2)
print(line(2))
print(line.table(1,5,4))

line = Line(-1,2)
print(line(2))
print(line.table(-1,5,10))

line = Line(3,4)
print(line(2))
print(line.table(1,5,15))

line = Line(3,4)
print(line(2))
print(line.table(1,5,0))

line = Line(3,4)
print(line(2))
print(line.table(1,1,15))
