import numpy as np
from sklearn import neighbors, datasets
import matplotlib.pyplot as plt
from qn2 import five_number_summary
from sklearn.preprocessing import MinMaxScaler

def normalize_minmax(data):
    #Check if is 2D array
    array = len(data.shape)
    if array != 2:
        return None
    else:
        ls = []
        #scaler = MinMaxScaler()
        #scaler.fit(data)
        #return scaler.transform(data)
        for i in range(data.shape[1]):
            row = data[:,i]
            #print(row)
            #print(np.max(row), np.min(row))
            row = (row - np.min(row))/(np.max(row)-np.min(row))
            ls.append(row)
        #print(np.array(ls))
        return np.array(ls).transpose()

bunchobject = datasets.load_breast_cancer()
cols = [1,7]
some_columns = bunchobject.data[:,cols]
snorm = normalize_minmax(some_columns)
#print("normalized",five_number_summary(snorm)) 
# can use ndim to check for dimensions
