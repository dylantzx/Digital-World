import numpy as np
from sklearn import neighbors, datasets
import matplotlib.pyplot as plt
from qn1 import *
from qn3 import *
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

bunchobject = datasets.load_breast_cancer()

def knn_classifier_full(bunchobject, feature_list, size, seed): 
    #step 2
    data = bunchobject.data[:,feature_list]
    #print(data.shape)
    #step 3 
    norm_data = normalize_minmax(data)
    class_labels = bunchobject.target
    #step 4
    #Divide model into 3 sets, training set, validation set and test set
    #Typical split is 60%, 20%, 20%
    #In this step, data_part2 and target_part2 contains 40% of records
    data_train, data_part2, target_train, target_part2 = train_test_split(norm_data, class_labels, test_size=size, random_state=seed) 
    #print(data_part2.shape, target_part2.shape)
    #call train_test_split() again to split data_part2 and target_part2 into 2 sets of 20% each
    data_validation, data_test, target_validation, target_test = train_test_split(data_part2, target_part2, test_size=0.5, random_state=seed) 
    #print(data_test.shape, target_test.shape)
    labels = [1,0]
    #step 5
    acc = []
    for k in range(1,21):
        clf = neighbors.KNeighborsClassifier(n_neighbors = k) 
        clf.fit(data_train, target_train) 
        validation_predicted = clf.predict(data_validation)
        accuracy = accuracy_score(target_validation, validation_predicted)
        acc.append(accuracy)
    #print(acc)
    max_acc = max(acc)
    #print(max_acc)
    value = acc.index(max_acc) + 1
    print(type(value))
    
    clf = neighbors.KNeighborsClassifier(n_neighbors = value) 
    clf.fit(data_train, target_train) 
    validation_predicted = clf.predict(data_validation)
    
    clf = neighbors.KNeighborsClassifier(n_neighbors = value) 
    clf.fit(data_train, target_train) 
    target_predicted = clf.predict(data_test)
   
    #step6
    out_results = {"best k": value, "validation set": get_metrics(target_validation, validation_predicted, labels), "test set": get_metrics(target_test, target_predicted, labels)}
    return out_results

features = range(20) 
results = knn_classifier_full(bunchobject, features, 0.40, 2752) 
print(results) 


