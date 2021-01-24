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

a = [[1 ,2 ,3] , [4 ,5 ,6] , [7 ,8 ,9]]
print(transpose_matrix( a ))
a = [[-11 ,12 ,3] , [4 ,-5 ,6]]
print(transpose_matrix( a ))
a = [[1 ,2 ] , [10 ,5 ] , [0,0]]
print(transpose_matrix( a ))
