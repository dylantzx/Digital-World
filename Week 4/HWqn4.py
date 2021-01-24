def most_frequent(lst):
    mydict = {}
    count=0
    most_freq = []
    for element in lst:
        mydict[element] = mydict.get(element,0)+1 #initialize value as 0
        if mydict[element] >= count:
            count = mydict[element]
    
    for key,value in mydict.items():
        
        if value == count:
            most_freq.append(key)
            
    
    return "most_frequent = {}".format(most_freq)

inp = [2,3,40,3,5,4,-3,3,3,2,0]
print(most_frequent(inp))
inp = [9,30,3,9,3,2,4]
print(most_frequent(inp))
