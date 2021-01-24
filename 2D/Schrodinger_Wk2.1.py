import numpy as np
import scipy.constants as c

def deg_to_rad(deg):
    radians=np.around(np.radians(deg), decimals=5)
    return radians
 
def rad_to_deg(rad):
    degrees=np.around(np.degrees(rad),decimals=5)
    return degrees

print(deg_to_rad(90)-1.5708) 
print(deg_to_rad(180)-3.14159) 
print(deg_to_rad(270)-4.71239) 
print(rad_to_deg(3.14)-179.90875) 
print(rad_to_deg(3.14/2.0)-89.95437) 
print(rad_to_deg(3.14*3/4)-134.93156)


