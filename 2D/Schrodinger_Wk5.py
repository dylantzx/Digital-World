import numpy as np
import scipy.constants as c

a = c.physical_constants['Bohr radius'][0]

def spherical_to_cartesian(r,theta,phi):
    x = np.around(r*(np.sin(theta))*np.abs(np.cos(phi)), decimals = 5)
    y = np.around(r*np.sin(theta)*np.sin(phi) , decimals = 5)
    z = np.around(r*np.cos(theta), decimals = 5)
    return x, y ,z

def cartesian_to_spherical(x, y, z):
    rho = np.around(np.sqrt(x**2+y**2+z**2), decimals = 5)
    theta = np.around(np.arccos(z/rho), decimals = 5)

    if x == 0:
        if y == 0:
            phi = 0.0
            
        elif y < 0:
            phi = -np.pi / 2
                
        else:
            phi = np.pi / 2
            
    else:
        phi = np.arctan(y / x)
        
    return rho, theta, round(phi,5)
    

def angular_wave_func(m,l,theta,phi):

    if l == 0:
        if m==0:
            y = np.sqrt(1/(4*np.pi))
            y = np.complex(round(y.real,5))

    elif l == 1:
        
         if m == 0: 
            y = np.sqrt(3/(4*np.pi))*np.cos(theta)
            y = np.complex(round(y.real,5))
            
         elif m == 1:
             y = -np.sqrt(3/(8*np.pi))*np.sin(theta)*np.exp(m*1j*phi)
             y = round(y,5)

         else:
             y = np.sqrt(3/(8*np.pi))*np.sin(theta)*np.exp(m*1j*phi)
             y = round(y,5)

    else:

        if m == 0:
            y = np.sqrt(5/(16*np.pi))*(3*(np.cos(theta)**2)-1)
            y = np.complex(round(y.real,5))

        elif m == 1:
            y = -np.sqrt(15/(8*np.pi))*np.sin(theta)*np.cos(theta)*np.exp(m*1j*phi)
            y = round(y,5)

        elif m == -1:
            y = np.sqrt(15/(8*np.pi))*np.sin(theta)*np.cos(theta)*np.exp(m*1j*phi)
            y = round(y,5)
            
        elif m == 2:
            y = np.sqrt(15/(32*np.pi))*(np.sin(theta)**2)*np.exp(m*1j*phi)
            y = round(y,5)
            
        else:
            y = np.sqrt(15/(32*np.pi))*(np.sin(theta)**2)*np.exp(m*1j*phi)
            y = round(y,5)
            
    return y

def radial_wave_func(n,l,r):
    if l == 0:
        if n == 1:
            R = 2*np.exp(-r/a)
        elif n == 2:
            R = 1/np.sqrt(2)*(1-r/(2*a))*np.exp(-r/(2*a))
        else:
            R = 2/(81*np.sqrt(3))*(27-18*(r/a)+2*(r/a)**2)*np.exp(-r/(3*a))
    elif l == 1:
        if n == 2:
            R = (1/np.sqrt(24))*(r/a)*np.exp(-r/(2*a))
        elif n == 3:
            R = (4/(81*np.sqrt(6)))*(6*(r/a)-(r/a)**2)*np.exp(-r/(3*a))
    elif l == 2:
        if n == 3:
            R = (4/(81*np.sqrt(30)))*np.exp(-r/(3*a))*((r/a)**2)
                
    return round(R,5)

def mgrid3d(xstart, xend, xpoints, 
            ystart, yend, ypoints, 
            zstart, zend, zpoints):
    xr = []
    yr = []
    zr = []
    xval = xstart
    xcount = 0

    # calculate the step size for each axis
    xstep=(xend-xstart)/(xpoints-1)
    ystep=(yend-ystart)/(ypoints-1)
    zstep=(zend-zstart)/(zpoints-1)
    
    while xcount < xpoints:
        # initialize y points
        ycount=0
        yval=ystart
        
        # create temporary variable to store x, y and z list
        xrow_second = []
        yrow_second = []
        zrow_second = []
    
        while ycount < ypoints:
            # initialize z points
            zcount=0
            zval=zstart
            
            # create temporary variable to store the inner x, y, and z list
            xrow_inner = []
            yrow_inner = []
            zrow_inner = []
        
            while zcount < zpoints:
                # add the points x, y, and z to the inner most list
                xrow_inner.append(xval)
                yrow_inner.append(yval)
                zrow_inner.append(zval)
            
                # increase z point
                zval+=zstep
                zcount+=1
            # add the inner most lists to the second lists
            xrow_second.append(xrow_inner)
            yrow_second.append(yrow_inner)
            zrow_second.append(zrow_inner)
        
            # increase y point
            yval+=ystep
            ycount+=1
        # add the second lists to the returned lists
        xr.append(xrow_second)
        yr.append(yrow_second)
        zr.append(zrow_second)
    
        # increase x point
        xval+=xstep
        xcount+=1
        
    return np.array([xr, yr, zr])

def hydrogen_wave_func(n,l, m, roa, Nx, Ny, Nz):
    #e.g.: vfunc = np.vectorize(cartesian_to_spherical)
    xstart, ystart, zstart = -roa, -roa, -roa
    xend, yend, zend = roa, roa, roa
    xpoints, ypoints, zpoints = Nx, Ny, Nz
    xx, yy, zz = mgrid3d(xstart, xend, xpoints, 
            ystart, yend, ypoints, 
            zstart, zend, zpoints)
    
    v_r, v_theta, v_phi = (np.vectorize(cartesian_to_spherical))(xx, yy, zz)
    v_ra=v_r * a
    v_rad = (np.vectorize(radial_wave_func))
    v_y = (np.vectorize(angular_wave_func))
    mag = np.vectorize(np.absolute)
    
    
    #######################
    
    if m < 0:
        
        Y = (1j/(np.sqrt(2)))*((v_y(m,l,v_theta,v_phi)) - ((-1)**(m))*v_y(-m,l,v_theta,v_phi))
        

    elif m == 0:
        
        Y = v_y(m,l,v_theta,v_phi)
        
        
    else:
        
        Y = (1/(np.sqrt(2)))*(v_y(-m,l,v_theta,v_phi) + ((-1)**(m))*v_y(m,l,v_theta,v_phi))
        
    
    #######################
    density = (mag(Y) * mag(v_rad(n,l,v_ra)))**2
 
    return np.around(xx,5), np.around(yy,5), np.around(zz,5), np.around(density, 5)

"""
###Test:

print('Test 1')
x,y,z,mag = hydrogen_wave_func(2 ,1 ,1 ,8 ,2 ,2 ,2)
print('x, y, z:')
print(x, y, z)
print('mag:')
print(mag)

print('\n')
print('Test 2')
x,y,z,mag = hydrogen_wave_func(2, 1, 1, 5, 3, 4, 2)
print('x, y, z:')
print(x, y, z)
print('mag:')
print(mag)


print('\n')
print('Test 3')
x,y,z,mag = hydrogen_wave_func(2 ,0 ,0 ,3 ,5 ,4 ,3)
print('x, y, z:')
print(x, y, z)
print('mag:')
print(mag)
"""

