def longest_common_prefix(string1, string2):
    output = ""
    length1=len(string1)
    length2=len(string2)
    if length1 >= length2:
        short = length2
    else:
        short = length1
        
    for num in range(short):
        if string1[num] != string2[num]:
            break
        elif string1[num] == string2[num]:
            output+=string1[num]
    return output

print("longest_common_prefix('distance','disinfection')")
ans = longest_common_prefix('distance','disinfection')
print(ans)
print("longest_common_prefix('testing','technical')")
ans = longest_common_prefix('testing','technical')
print(ans)
print("longest_common_prefix('drinking','drinker')")
ans = longest_common_prefix('drinking','drinker')
print(ans)
print("longest_common_prefix('rosses','crosses')")
ans = longest_common_prefix('rosses','crosses')
print(ans)
print("longest_common_prefix('distancetion','distance')")
ans = longest_common_prefix('distancetion','distance')
print(ans)
