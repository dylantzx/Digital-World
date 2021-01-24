def get_fundamental_constants(f):
    constants = {}
    i=0
    for line in f:
        data = line.split()
        if i>1:
            constants[data[0]]=float(data[1])
        i+=1   
    f.close()
    return constants

fo = open("constants.txt", "r")
print(get_fundamental_constants(fo))
