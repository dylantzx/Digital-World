def split_sentences(f):
    string = f.read()
    #string = string.replace("!","!\n")
    string = string.replace("? ",". ")
    punc = "!@#$%^&*()_+{}:?><|\][;'/.,`~=-"
    new_ls = []
    count = 0
    length = len(string)
    print(string)
    sentence = True
    for idx in range(length):
        if "." in string[idx]:
            num = idx
            #print(num, string[num],string[num+1], string[num+2])
            if string[num+1] == " " and string[num+2].islower():
                sentence = False
            elif string[num+1] == " " and string[num+2].isupper():
                #print(string[num-3:num+1])
                #print(("Mr." or "Mrs." or "Dr." or "Jr.") in string[num-3:num+1])
                if (("Mr." or "Mrs." or "Dr." or "Jr.") in string[num-3:num+1]) or (("Mr." or "Mrs." or "Dr." or "Jr.") in string[num-2:num+1]):
                    sentence = False
                else:
                    sentence = True
                    
            elif string[num+1].isalnum():
                sentence = False
            elif string[num+1] in punc:
                sentence = False
            #print(num, sentence)
            
            if sentence == True:
                #print(count, num)
                #print(new_ls)
                #print(count, num, sentence)
                new_ls.append(string[count:num+1])
                count = num+2
                #print(num,count, sentence)
    new_ls.append(string[count:-1])
                       
        
    print(new_ls)
    
f=open("split.txt","r")
split_sentences(f)
