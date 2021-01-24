import numpy as np
import matplotlib.pyplot as plt

def five_number_summary(x):
    ls = []
    keys = ["minimum", "first quartile", "median", "third quartile", "maximum"]
    num_of_col = len(x[0])
    for num in range(num_of_col):
        dic = {}
        col = x[:,[num]]
        #print(col)
        mx = np.max(col)
        mn = np.min(col)
        md = np.percentile(col,50)
        fq = np.percentile(col,25)
        tq = np.percentile(col,75)
        val = [mn, fq, md, tq, mx]
        #print(val)
        for i in range(len(keys)):
            dic[keys[i]] = val[i]
        #print(dic)
        ls.append(dic)
        #print(ls)
    #print(ls)
    return ls

matrix = np.array([[1,2,3],[2,3,2],[3,1,1],[4,2,3],[5,6,3],[6,4,1]])
#print(matrix)
col_no = [0,1,2]
col_matrix = matrix[:,col_no]
#print(col_matrix)
data = five_number_summary(col_matrix)
#print(data)
#print(matrix)
#plt.boxplot(matrix)
#plt.show()

