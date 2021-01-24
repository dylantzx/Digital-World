import numpy as np

"""
a = np.array([[3,1],[1,2]])
b = np.array([9,8])
x = np.linalg.solve(a,b) #helps solve ax=b
print(x)
print(type(a), type(b), type(x))
print(a.shape, b.shape, x.shape)
print("#############")

###################################
a1 = a[0,:] # left side indicate row, right side indicates column
print(a1, a1.shape) #but using an integer will result in same output
a2 = a[:,0]
print(a2, a2.shape)
print("#############")

###################################
ls = [1] 
a3 = a[ls,:] #using a list with the idx, on left, a3 will print a[1] as row 
print(a3, a3.shape)  
a4 = a[:,ls] #using a list with the idx, on right, a3 will print column 1 of a
print(a4, a4.shape)
print("#############")

###################################
#transforming 1D array to 2D array
#1D array has only 1 number in the tuple 
b1 = b.reshape(1, b.size) #now b1 is a 1 by n 2D array
print(b1, b1.shape)
b2 = b.reshape(b.size, 1) #now b2 is a n by 1 2D array
print(b2, b2.shape)
print("#############")

###################################
m = [ [1,-1,0], [-1, 2, -1], [0, -1, 1] ]
M = np.array(m)
w, v = np.linalg.eig(M)#linalg function can turn m into a numpy array
print(w,v)
print(type(w), type(v))
print(w.shape, v.shape) #w is 1D, v is 2D
v_c0 = v[:,0]
v_c1 = v[:,[1]]
print(v_c0, v_c0.shape)
print(v_c1, v_c1.shape)
print("#############")
"""
###################################
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets #Scikit-learn is package for ML

bunchobject = datasets.load_breast_cancer() #returns instance of Bunch class and stors in variable bunchobject
print(bunchobject.DESCR)
print(bunchobject.data) #Shows data but holds no meaning yet
print(bunchobject.feature_names)
print(bunchobject.target_names)
print(bunchobject.data.shape)
#569 records, 30 features, 2 categories in target variable
#5th feature from 0 is mean compactness

print("### extract info from each feature ###")
column_index = [1]
print(bunchobject.feature_names[column_index])
feature_vals_in_column = bunchobject.data[:,column_index]
print(feature_vals_in_column)
print(np.min(feature_vals_in_column), np.max(feature_vals_in_column))

print("### extract info from each record ###")
row_index = [1]
print(bunchobject.feature_names)
record_vals_in_row = bunchobject.data[row_index,:]
print(record_vals_in_row)
print(bunchobject.target[row_index])

unique, counts = np.unique(bunchobject.target, return_counts = True)
for i in unique:
    print(i, bunchobject.target_names[i], counts[i])



