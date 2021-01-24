import numpy as np 
def spherical_to_cartesian(r,theta,phi):
    x = np.around(r*(np.sin(theta))*np.abs(np.cos(phi)), decimals = 5)
    y = np.around(r*np.sin(theta)*np.sin(phi) , decimals = 5)
    z = np.around(r*np.cos(theta), decimals = 5)
    return x, y ,z
def cartesian_to_spherical(x, y, z):
    r = np.around(np.sqrt(x**2+y**2+z**2), decimals = 5)
    theta = np.around(np.arccos(z/r), decimals = 5)
    
    if x> 0:
        phi = np.around(np.arctan(y/x), decimals = 5)
    elif y>0: 
        phi = np.around(np.arccos(x/np.sqrt(x**2+y**2)), decimals = 5)
    elif y<0: 
        phi = np.around(-np.arccos(x/np.sqrt(x**2+y**2)), decimals = 5)
    else:
        phi = 0.0
    return r, theta, phi
