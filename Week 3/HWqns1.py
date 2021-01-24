def temp_convert(choice, temp):
    
    if choice == "C":
        new_temp = (temp-32)*5/9
    elif choice == "F":    
        new_temp = temp*9/5+32
    else:
        return None
    return new_temp
    
print (" Test case 1: C = 32 " )
ans = temp_convert ( "F" , 32)
print ( ans )

print (" Test case 2: C = -40 " )
ans = temp_convert ( "F" , -40)
print ( ans )

print (" Test case 3: C = 212 " )
ans = temp_convert ( "F" , 212)
print ( ans )
