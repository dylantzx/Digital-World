def list_sum(inp):
    #inp is a list of numbers
    if len(inp) == 0:
        return 0.0
    total=0
    pos =0
    while pos <= len(inp)-1:
        total = total + inp[pos]
        pos+=1
    return total


print("Test case 1: [4.25,5.0,10.75]")
ans=list_sum([4.25,5.0,10.75])
print(ans)
print("Test case 2: [5.0]")
ans=list_sum([5.0])
print(ans)
print("Test case 3: []")
ans=list_sum([])
print(ans)
