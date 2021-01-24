import numpy as np
"""
def angular_wave_func(m,l,theta,phi):
    if m == 0:
        if l == 0:
            y = 1/(np.sqrt(4*np.pi))
                        
        elif l == 1:
            y = np.sqrt(3
                        /(4*np.pi))*np.cos(theta)
            
        else:
            y = np.sqrt(5/(4*np.pi))*(3/2*(np.cos(theta)**2)-1/2)   

        y = np.complex(round(y.real,5))
            
    elif m == 1:
        if l == 1:
            y = -np.sqrt(3/(8*np.pi))*np.sin(theta)*np.exp(np.complex(0,phi))
            y = round(y,5)
           
    return y"""
def angular_wave_func(m,l,theta,phi):

    if l == 0:
            y = 1/(np.sqrt(4*np.pi))
            y = np.complex(round(y.real,5))

    elif l == 1:
        
         if m == 0: 
            y = np.sqrt(3/(4*np.pi))*np.cos(theta)
            y = np.complex(round(y.real,5))
            
         elif m == 1:
             y = -np.sqrt(3/(8*np.pi))*np.sin(theta)*np.exp(np.complex(0,phi))
             y = round(y,5)

         else:
             y = np.sqrt(3/(8*np.pi))*np.sin(theta)*np.exp(-np.complex(0,phi))
             y = round(y,5)

    else:

        if m == 0:
            y = np.sqrt(5/(4*np.pi))*(3/2*(np.cos(theta)**2)-1/2)
            y = np.complex(round(y.real,5))

        elif m == 1:
            y = -np.sqrt(15/(8*np.pi))*np.sin(theta)*np.cos(theta)*np.exp(np.complex(0,phi))
            y = round(y,5)

        elif m == -1:
            y = np.sqrt(15/(8*np.pi))*np.sin(theta)*np.cos(theta)*np.exp(-np.complex(0,phi))
            y = round(y,5)
            
        elif m == 2:
            y = np.sqrt(15/(32*np.pi))*(np.sin(theta)**2)*np.exp(np.complex(0,2*phi))
            y = round(y,5)
            
        else:
            y = np.sqrt(15/(32*np.pi))*(np.sin(theta)**2)*np.exp(-np.complex(0,2*phi))
            y = round(y,5)
            
    return y

print(angular_wave_func(0,0,0,0))
print(angular_wave_func(0,1,np.pi,0))
print(angular_wave_func(1,1,np.pi/2,np.pi))
print(angular_wave_func(0,2,np.pi,0))
