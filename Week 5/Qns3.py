#function calling itself
#divide and conquer
#Base case
#Recursive case

def sum_rec(list_n):
    
    if len(list_n) == 1:
        #base case
        return list_n[0]
    else:
        #recursive case
        return list_n[0] + sum_rec(list_n[1:])

a = [1,2,3,7,-1,5]
print(sum_rec(a))

def fact_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact_rec(n-1)

print(fact_rec(5))
