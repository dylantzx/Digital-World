import math
def approx_ode(h,t0,y0,tn):
    # Inputs - h  : step size
    #          t0 : initial t value (at step 0)
    #          y0 : initial y value (at step 0)
    #          tn : t value at step n
    # Add your code below!
    t=t0
    y=y0
    while t < tn:
        f_ty = 3 + math.exp(-t)-0.5*y
        y+= h* f_ty
        t+=h
        t=round(t,1)
    return y

print ("approx_ode (0.1 , 0 , 1 , 5)")
ans = approx_ode (0.1 , 0 , 1 , 5)
print ( "Output : " , ans )


print ( " approx_ode (0.1 , 0 , 1 , 2.5) ")
ans = approx_ode (0.1 , 0 , 1 , 2.5)
print ( " Output : " , ans )


print ( " approx_ode (0.1 , 0 , 1 , 3) ")
ans = approx_ode (0.1 , 0 , 1 , 3)
print ( " Output : " , ans )


print ( " approx_ode (0.1 , 0 , 1 , 1) ")
ans = approx_ode (0.1 , 0 , 1 , 1)
print ( " Output : " , ans )


print ( " approx_ode (0.1 , 0 , 1 , 0) ")
ans = approx_ode (0.1 , 0 , 1 , 0)
print ( " Output : " , ans )

    



   
