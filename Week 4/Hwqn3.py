def multiplication_table(n):
    if n < 1:
        return None

    else:
        multiplication_table_ls = []
        for num in range(1,n+1):
            inner_ls = []
            for inner_num in range(1,n+1):
                inner_ls.append(inner_num*num)
            multiplication_table_ls.append(inner_ls)
    
    return multiplication_table_ls

print(multiplication_table(7))
print(multiplication_table(1))
print(multiplication_table(0))
print(multiplication_table(2))
print(multiplication_table(-1))
