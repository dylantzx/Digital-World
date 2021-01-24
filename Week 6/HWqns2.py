def uncompress(string):
    strg=""
    count=1
    length = len(string)
    for num in string[::2]:
        int_num=int(num)
        strg += string[count]*int_num
        #print(int_num, string[count],strg)
        count+=2
    return strg
print(uncompress("2a5b1c"))
print(uncompress("1a1b2c"))
print(uncompress("1a9b3b1c"))

