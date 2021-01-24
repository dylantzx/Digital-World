def find_anagram(f):
    #string = f.read()
    #print(string)
    lst= []
    dic = {}
    inner_list = []
    words = ['abel','alger','angel','evil','caret','elan']
    anagram = []
    
    for line in f:
        line = line.lower().strip().replace("\n","")
        if line.isalpha():
            lst.append(line)
    for word in lst:
        new_word = "".join(sorted(word))
        #print(word, new_word)
        dic[new_word]= dic.get(new_word,0) + 1

        if dic[new_word] >1:
            inner_list.append(new_word)
            if new_word != word:
                inner_list.append(word)
    count=0
    while count < 6:
        ls_i=[]
        dic_inner = {}
        for ana in inner_list[:]:
            dic_i = sort(ana,words,dic_inner,count)
            if dic_i != None:
                for value in dic_i.values():
                    if value not in ls_i:
                        ls_i.append(value)
        #print(dic_inner)
        #print(ls_i)
        if len(ls_i) !=0:
            anagram.append(ls_i)
        
        count+=1
    print(anagram)
    f.close()
    
def sort(ana,words,dic_inner,count):
    if sorted(ana) == sorted(words[count]):
        dic_inner[ana] = ana
        return dic_inner

file = open("anagram.txt","r")
find_anagram(file)
