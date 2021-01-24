import math

"""def area_of_triangle (p1 ,p2 ,p3):
    #Get length of the sides of the triangle
    side1 = math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
    side2 = math.sqrt((p3.x-p2.x)**2+(p3.y-p2.y)**2)
    side3 = math.sqrt((p3.x-p1.x)**2+(p3.y-p1.y)**2)
    s = (side1 + side2 + side3)/2
    area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
    return round(area, 2)
    
class Coordinate:
    x = 0.0
    y = 0.0
print ("Test Case 1")
p1 = Coordinate()
p1 . x =1.5
p1 . y = -3.4
p2 = Coordinate()
p2 . x =4.6
p2 . y =5
p3 = Coordinate()
p3 . x =9.5
p3 . y = -3.4

ans = area_of_triangle (p1 , p2 , p3)
print(ans)

print ("Test Case 2")
p1 = Coordinate()
p1 . x =2.0
p1 . y = -3.4
p2 = Coordinate()
p2 . x =4.6
p2 . y =5
p3 = Coordinate()
p3 . x =9.5
p3 . y = -1.4

ans = area_of_triangle (p1 , p2 , p3)
print(ans)

print ("Test Case 3")
p1 = Coordinate()
p1 . x =1.5
p1 . y =3.4
p2 = Coordinate()
p2 . x =4.6
p2 . y =5
p3 = Coordinate()
p3 . x = -1.5
p3 . y =3.4

ans = area_of_triangle (p1 , p2 , p3)
print(ans)

print ("Test Case 4")
p1 = Coordinate()
p1 . x = -1.5
p1 . y =3.4
p2 = Coordinate()
p2 . x =4.6
p2 . y =5
p3 = Coordinate()
p3 . x =4.3
p3 . y = -3.4

ans = area_of_triangle (p1 , p2 , p3)
print(ans)"""

def area_of_triangle (p1 ,p2 ,p3):
    #Get length of the sides of the triangle
    side1 = math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
    side2 = math.sqrt((p3.x-p2.x)**2+(p3.y-p2.y)**2)
    side3 = math.sqrt((p3.x-p1.x)**2+(p3.y-p1.y)**2)
    s = (side1 + side2 + side3)/2
    area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
    return round(area, 2)

class Coordinate:
    x = 0.0
    y = 0.0
p1 = Coordinate()
p1 . x = float(input("Enter x coordinate of the first point of a triangle: "))
p1 . y = float(input("Enter y coordinate of the first point of a triangle: "))
p2 = Coordinate()
p2 . x = float(input("Enter x coordinate of the second point of a triangle: "))
p2 . y = float(input("Enter y coordinate of the second point of a triangle: "))
p3 = Coordinate()
p3 . x = float(input("Enter x coordinate of the third point of a triangle: "))
p3 . y = float(input("Enter y coordinate of the third point of a triangle: "))
ans = area_of_triangle (p1 , p2 , p3)
print("The area of the triangle is ", ans)
