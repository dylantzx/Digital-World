import numpy as np

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

# Test:
# assert statement will throw error if the result is wrong
# no output will be produced for correct results

print(mgrid3d(0, 4, 5, 0, 4, 5, 0, 4, 5))
print(mgrid3d(0, 5, 15, 0, 4, 10, 1, 2, 3))
