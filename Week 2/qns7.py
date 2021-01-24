def is_in_square(s1,a,s2,b):
    #find centre of lines for each square
    rightline1 = s1.x + a
    leftline1 = s1.x - a
    topline1 = s1.y + a
    bottomline1 = s1.y - a
    rightline2 = s2.x + b
    leftline2 = s2.x - b
    topline2 = s2.y + b
    bottomline2 = s2.y - b

    #check if left line of square 2 is between left and right lines of square 1 and top line of square 2 is between bottom and top line of square 1 
    if (leftline2 >= leftline1 and leftline2 <= rightline1) and (topline2 >= bottomline1 and topline2 <= topline1):
        print("True")
        
    else:
        print("False")
    
class Coordinate:
    x=0
    y=0
s1 = Coordinate()
s1.x, s1.y = 10, 10
s2 = Coordinate()
s2.x, s2.y = 20, 10
is_in_square(s1,5,s2,4)



