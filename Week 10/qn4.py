import numpy as np
from sklearn import neighbors, datasets
import matplotlib.pyplot as plt
from qn1 import *
from qn3 import *
from sklearn.model_selection import train_test_split

def display_bar_chart(positions, counts, names, title_name = 'default'):
    index = np.arange(len(names))
    plt.bar(positions,counts, 0.4)
    plt.title(title_name)
    plt.xticks(index, names)
    plt.show()
    
bunchobject = datasets.load_breast_cancer()
unique, counts = np.unique(bunchobject.target, return_counts = True)
#display_bar_chart(unique, counts, bunchobject.target_names)

def knn_classifier(bunchobject, feature_list, size, seed, k): 
    #step 2
    data = bunchobject.data[:,feature_list]
    #step 3 
    norm_data = normalize_minmax(data)
    class_labels = bunchobject.target
    #step 4 
    data_train, data_test, target_train, target_test = train_test_split(norm_data, class_labels, test_size=size, random_state=seed) 
    #print(data_train.shape, data_test.shape)
    #print(target_train.shape, target_test.shape)
    labels = [1,0]
    #step 5 
    clf = neighbors.KNeighborsClassifier(n_neighbors = k) 
    clf.fit(data_train, target_train) 
    target_predicted = clf.predict(data_test)
    #step6
    results = get_metrics(target_test, target_predicted, labels)
    #print(results)
    return results

features = range(20) 
results = knn_classifier(bunchobject, features, 0.40, 2752, 3) 
print(results) 

