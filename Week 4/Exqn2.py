def interlock(word1,word2,word3):
    ans = word1, word2, word3
    length1 = len(word1)
    length2 = len(word2)
    #if word 1 and word 2 interlock and generates word 3, True
    #if word1,2,3 are left blank, False
    #words length not same, empty string, cannot interlock
    if length1 != length2 or length1 == 0 or length2 == 0 :
        return False
    else:
        string = ""
        i=0
        for char in word2:
            string += word1[i]
            string += char
            i+=1
        if string == word3:
            return True
        else:
            return False
            

#Test case 1
ans = interlock('shoe', 'cold', 'schooled')
print(ans) 

#Test case 2
ans = interlock('shoes', 'cold', 'schooled')
print(ans)

#Test case 3
ans = interlock('', 'cold', 'schooled')
print(ans)

#Test case 4
ans = interlock('shoes', 'cold', '')
print(ans)

#Test case 5
ans = interlock('', '', '')
print(ans)

#Test case 6
ans = interlock('can', 'his', 'chains')
print(ans) 
