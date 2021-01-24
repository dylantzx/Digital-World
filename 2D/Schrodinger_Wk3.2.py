import scipy.constants as c
import numpy as np 

a = c.physical_constants['Bohr radius'][0]
def radial_wave_func(n,l,r):
    if l == 0:
        if n == 1:
            R = 2*np.power(1/a,3/2)*np.exp(-r/a)
    elif l == 1:
        if n == 2:
            R = (1/(2*np.sqrt(6)))*np.power(1/a,3/2)*(r/a)*np.exp(-r/(2*a))
        elif n == 3:
            R = (4/(81*np.sqrt(6)))*np.power(1/a,3/2)*(6*(r/a)-(r/a)**2)*np.exp(-r/(3*a))
    R = R/np.power(a,-3/2)
    return round(R,5)

print(radial_wave_func(1,0,a))
print(radial_wave_func(2,1,a))
print(radial_wave_func(2,1,2*a))
print(radial_wave_func(3,1,2*a))
