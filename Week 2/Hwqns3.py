import math
def area_vol_cylinder(radius,length):
    area = radius * radius * math.pi
    volume = area * length
    return round(area,2), round(volume,2)
print ( area_vol_cylinder (1.0 ,2.0) )
print ( area_vol_cylinder (2.0 ,2.3) )
print ( area_vol_cylinder (1.5 ,4) )
print ( area_vol_cylinder (2.2 ,5.0) )
