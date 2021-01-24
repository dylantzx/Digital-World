def binary_to_decimal(binstr):
    ans = 0
    i=0
    for char in binstr[-1::-1]:
        if char == "1":
            ans += 2**i
        i+=1 
    return ans
print(binary_to_decimal('100'))
print(binary_to_decimal('101'))
print(binary_to_decimal('10001'))
print(binary_to_decimal('10101'))
