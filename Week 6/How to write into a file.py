f = open("test.txt", "w")
f.write("abc")
f.close()

##### Writing in a new line #####
f = open("test.txt", "w")
f.write("abc")
f.write("\ndef")
f.close()
#################################

##### formating while writing into a text file #####
x = list(range(10))
f = open("test.txt", "w")
for el in x:
    y = el*el
    f.write("{:f}\t{:f}\n".format(el,y))
f.close()
