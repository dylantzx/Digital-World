########################
# Function Definition #
########################
def is_palindrome(inp):
    #inp is an integer
    inpstr = str(inp)
    
    n = len(inpstr)
    #Init Block
    left = 0 # zero is the inde of the first element
    right = n - 1 # n - 1 is the index of the last element
    #Condition Block
    while left < n // 2:
        #Block A
        if inpstr[left] != inpstr[right]:
            return False
        # modify condition
        left += 1
        right -= 1
    #Block B, after iteration, after finishing comparison with all 
    return True
    

################################
# Function Calling/Invocation #
################################
print(is_palindrome(1))
print(is_palindrome(22))
print(is_palindrome(4321234))
print(is_palindrome(4321134))



"""Convert number to a string, then to a list, after
that convert list that is in string form into int """
numberlist1 = [int(a) for a in list(str(12312312133))]
numberlist = list(map(int, str(122312313)))
print(numberlist1)
print(numberlist)
                     
