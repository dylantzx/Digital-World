def f_to_c(f):
    c=(f-32)*5/9
    return c

def f_to_c_approx(f):
    C = (f-30)/2
    return C

def get_conversion_table_a():
    ls_ls = []
    #for 0,10,20...100
    for fahrenheit in range(0,110,10):
        ls = []
        C_exact = round(f_to_c(fahrenheit),1)
        C_approx = round(f_to_c_approx(fahrenheit),1)
        ls.append(fahrenheit)
        ls.append(C_exact)
        ls.append(C_approx)
        
    #list in list (f,c,C)
    #c and C to 1dp

        ls_ls.append(ls)
        
    return ls_ls
def get_conversion_table_b():
    ls_ls = []
    f_ls = []
    C_exact_ls = []
    C_approx_ls = []
    #for 0,10,20...100
    for fahrenheit in range(0,110,10):
        C_exact = round(f_to_c(fahrenheit),1)
        C_approx = round(f_to_c_approx(fahrenheit),1)
        f_ls.append(fahrenheit)
        C_exact_ls.append(C_exact)
        C_approx_ls.append(C_approx)        
    #list in list (f,c,C)
    #c and C to 1dp

    ls_ls.append(f_ls)
    ls_ls.append(C_exact_ls)
    ls_ls.append(C_approx_ls)
        
    return ls_ls

def transpose_matrix(a):
    transpose = []
    i=0 #individual element
    for m in range(len(a[i])):
        pos=0 #determines which sublist
        transpose_sub = []
        for n in range(len(a)):
            transpose_sub.insert( pos ,a[pos][i])
            pos+=1
        transpose.append(transpose_sub)
        i+=1
    return transpose

print(get_conversion_table_a())
print(get_conversion_table_b())
print(transpose_matrix(get_conversion_table_a()))

