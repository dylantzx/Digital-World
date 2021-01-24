def gcd(inp1,inp2):
    while inp2:
        print(inp1,inp2)
        inp1,inp2 = inp2, inp1%inp2
        print(inp1,inp2)
    return inp1
print(gcd(2148,128))
