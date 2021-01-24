def diff(p):
    dic = {}
    for key,value in p.items():
        if key == 0:
            continue
        else:
            newkey=key-1
            dic[newkey]=key*value
    
    return dic

p = {0: -3, 3:2, 5:-1}
print(diff(p))
p = {1: -3, 3:2, 5:-1,6:2}
print(diff(p))
p = {0: -3, 3:2, 8:2}
print(diff(p))
p = {0: -4, 2:12, 3:-2, 4:3, 8:2}
print(diff(p))
p = {0: -3, 1:12, 2:-2, 3:2, 10:2}
print(diff(p))
