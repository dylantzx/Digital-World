def minmax_in_list(i):
    if len(i) == 0:
        return None,None
    maxint = i[0]
    minint = i[0]
    pos = 1
    while pos < len(i):
        if maxint < i[pos]:
            maxint = i[pos]
        if minint > i[pos]:
            minint = i[pos]
        pos+=1
    return minint, maxint


print("Test case 1: [1,2,3,4,5]")
ans=minmax_in_list([1,2,3,4,5])
print(ans)

print("Test case 2: [1,1,3,0]")
ans=minmax_in_list([1,1,3,0])
print(ans)

print("Test case 3: [3,2,1]")
ans=minmax_in_list([3,2,1])
print(ans)

print("Test case 4: [0,10]")
ans=minmax_in_list([0,10])
print(ans)

print("Test case 5: [1]")
ans=minmax_in_list([1])
print(ans)

print("Test case 6: []")
ans=minmax_in_list([])
print(ans)

print("Test case 7: [1,1,1,1,1]")
ans=minmax_in_list([1,1,1,1,1])
print(ans)
