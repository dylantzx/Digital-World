def get_even_list(ls):
    new_list=[]
    pos=0
    while pos < len(ls):
        if ls[pos]%2==0:
            new_list.append(ls[pos])
        pos+=1
    return new_list

print ( " get_even_list ([1 ,2 ,3 ,4 ,5]) " )
ans = get_even_list ([1 ,2 ,3 ,4 ,5])
print ( ans )

print ( " get_even_list ([11 ,22 ,33 ,44 ,55]) " )
ans = get_even_list ([11 ,22 ,33 ,44 ,55])
print ( ans )

print ( " get_even_list ([10 ,20 ,30 ,40 ,50]) " )
ans = get_even_list ([10 ,20 ,30 ,40 ,50])
print ( ans )

print ( " get_even_list ([11 ,21 ,31 ,41 ,51]) " )
ans = get_even_list ([11 ,21 ,31 ,41 ,51])
print ( ans )
