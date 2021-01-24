import sys
def max_list(inlist):
    outlist = []
    for num_of_lists in range(len(inlist)):
        max_num = -sys.maxsize -1
        for num in range(len(inlist[num_of_lists])):
            if inlist[num_of_lists][num] > max_num:
                max_num = inlist[num_of_lists][num]
        outlist.append(max_num)
        
    return outlist

inlist = [[1,2,3],[4,5]]
print(max_list(inlist))
inlist = [[1,2,3],[4,5],[32,3,4]]
print(max_list(inlist))
inlist = [[3,4,5,2],[1,7],[8,0,-1],[2]]
print(max_list(inlist))
inlist = [[100],[1,7],[-8,-2,-1],[2]]
print(max_list(inlist))
inlist = [[3,4,5,2]]
print(max_list(inlist))
