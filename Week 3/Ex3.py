import math
def approx_pi(n):
    pi_value = 1103
    
    for i in range(1,n+1):
        factorial=1
        factorial_4=1
        for num in range(1,i+1):
            factorial = factorial*num
        for anum in range(1,(4*i)+1):
            factorial_4 = factorial_4*anum
        pi_value = pi_value + ((factorial_4)*(1103+26390*i))/((factorial)**4*396**(4*i))
    pi_value = pi_value *(2*math.sqrt(2)/9801)
    pi_value = 1/pi_value
    return pi_value


def approx_pi_with_math(n):
    pi_value = 1103
    
    for i in range(1,n+1):
        pi_value = pi_value + ((math.factorial(4*i))*(1103+26390*i))/((math.factorial(i))**4*396**(4*i))
    pi_value = pi_value *(2*math.sqrt(2)/9801)
    pi_value = 1/pi_value
    return pi_value

print(approx_pi(5))
print(approx_pi_with_math(5))
