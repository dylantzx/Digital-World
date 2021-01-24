def is_prime(n):
    counter=1
    while counter < n:
        if n%counter == 0 and n/counter != n:
            return False
        counter+=1
    return True

print ( " is_prime (2) " )
ans = is_prime (2)
print ( ans )

print ( " is_prime (3) " )
ans = is_prime (3)
print ( ans )

print ( " is_prime (7) " )
ans = is_prime (7)
print ( ans )

print ( " is_prime (9) " )
ans = is_prime (9)
print ( ans )

print ( " is_prime (21) " )
ans = is_prime (21)
print ( ans )
