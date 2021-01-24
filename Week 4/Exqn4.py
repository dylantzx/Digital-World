import random
def pi_approx_monte_carlo(n):
    c = 0
    s = 0
    for i in range(n):
        #num = random.random() #gives between [0,1)
        x,y = random.uniform(0,1),random.uniform(0,1) #gives between [0,1]
        r_square = x**2+y**2
        if r_square <= 1:
            c+=1
            s+=1
        else:
            s+=1
    pi = 4*c/s
    return round(pi,2)
ans = pi_approx_monte_carlo (100)
print(ans) #pi = 3.36
ans= pi_approx_monte_carlo (100000)
print(ans) #pi = 3.15
ans= pi_approx_monte_carlo (10000000) #( takes approx . 7 seconds )
print(ans) #pi = 3.14
