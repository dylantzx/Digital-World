###From right to left###
def reverse(strg):
    out = ""
    length = len(strg)
    for idx in strg[length-1::-1]:
        out += idx
    return out

print(reverse("I am testing"))
        
###From left to right###
def reverse_1(strg):
    out = ""
    length = len(strg)
    for idx in range(length):
        out = strg[idx] + out
    return out

print(reverse_1("I am testing"))
