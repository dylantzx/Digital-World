def mgrid2d(xstart, xend, xpoints, ystart, yend, ypoints):
    # initialize a list to store the grid points that will be returned
    xr=[]
    yr=[]
    
    # initialize the first x value
    xval = xstart
    
    # initialize a variable to count the number of x points
    xcount = 0
    
    # Calculate the step size for x and y, replace None with the right expression
    xstep = (xend-xstart)/(xpoints-1)
    ystep = (yend-ystart)/(ypoints-1)
    
    while xcount < xpoints:
        # initialize the first y value, replace None with the right value
        yval = ystart
        
        # initialize the variable to count the number of y points, replace None with the right value
        ycount = 0
        
        # initialize temporary lists
        xrow = []
        yrow = []
        
        while ycount < ypoints:
            # write code to add the current x value to the temporary x list
            xrow.append(xval)
        
            # write code to add the current y value to the temporary y list
            yrow.append(yval)
        
            # increase the y value by the step size in y
            yval+=ystep
        
            # increase the counter for the number of y points
            ycount+=1
        # Add the temporary x list to the final x list
        xr.append(xrow)
    
        # Add the temporary y list to the final y list
        yr.append(yrow)
    
        # increase x value by the step size in x
        xval+=xstep
    
        # increase the counter for the number of x points
        xcount+=1
        
    return xr,yr


print(mgrid2d(0, 4, 5, 0, 4, 5))
print(mgrid2d(0, 5, 15, 0, 4, 10))
