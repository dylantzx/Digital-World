import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn import neighbors, datasets
import matplotlib.pyplot as plt

def get_metrics(actual_targets, predicted_targets, labels):
    c_dict = {}
    c_matrix = confusion_matrix(actual_targets, predicted_targets, labels)
    tn, fp, fn, tp = confusion_matrix(actual_targets, predicted_targets, labels).ravel()
    
    t_records = round(sum(c_matrix.ravel()),3)
    accuracy = round((tn + tp)/t_records,3)
    sensitivity = round(tp/(tp+fn),3)
    fpr = round(fp/(fp+tn),3)
    
    keys = ["confusion matrix", "total records", "accuracy", "sensitivity", "false positive rate"]
    values = [c_matrix, t_records , accuracy, sensitivity, fpr]
    for i in range(len(keys)):
        c_dict[keys[i]] = values[i]  
    
    return c_dict

actual = ['cat', 'cat', 'cat', 'cat', 'bird', 'bird','bird','bird']
predicted = ['cat', 'cat', 'bird', 'bird', 'cat', 'bird', 'bird', 'bird']
labels = ['bird','cat'] #specify negative case followed by positive case
#positive case is what u want to predict and the more important category

#print(get_metrics(actual, predicted, labels))
# returns [[1,3],[2,2]] for bird, cat but if other way then is[[2,2],[1,3]]

