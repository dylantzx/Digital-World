import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors, datasets
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

def display_scatter(x,y,xlabel= 'x',ylabel='y',title_name = 'default'):
    plt.scatter(x,y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title_name)
    plt.show()

def multiple_linear_regression(bunchobject, x_index, y_index, order, size, seed):
    x = bunchobject.data[:,[x_index]]
    y = bunchobject.data[:,[y_index]]
    x_label = bunchobject.feature_names[x_index] 
    y_label = bunchobject.feature_names[y_index]
    poly = PolynomialFeatures(order, include_bias = False)
    c_data = poly.fit_transform(x)
    #print(c_data.shape)
    x_train, x_test, y_train, y_test = train_test_split(c_data , y, test_size = size ,random_state = seed) 
    #print(x_train.shape, y_train.shape)
    regr = linear_model.LinearRegression() 
    regr.fit(x_train, y_train) 
    y_pred = regr.predict(x_test)
    ms_error = mean_squared_error(y_test, y_pred)
    r_square = r2_score(y_test, y_pred)
    coef = regr.coef_
    inter = regr.intercept_
    #print(coef, inter, ms_error, r_square)
    results = {"coefficients": coef , "intercept": inter,"mean squared error": ms_error , "r2 score": r_square}

    return x_train[:,[0]], y_train, x_test[:,[0]], y_pred, results

def plot_linear_regression(x1, y1, x2, y2, x_label = "", y_label=""):
    plt.scatter(x1,y1,color = "black")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

bunchobject = datasets.load_breast_cancer()
x_index = 0
y_index = 3
x = bunchobject.data[:,[x_index]]
y = bunchobject.data[:,[y_index]]
x_label = bunchobject.feature_names[x_index] 
y_label = bunchobject.feature_names[y_index]
#display_scatter(x, y, x_label, y_label)
########################################################

x_train, y_train, x_test, y_pred, results = multiple_linear_regression(bunchobject,0,3,4,0.4,2752)
print(results)

#plot_linear_regression(x_train, y_train, x_test, y_pred, bunchobject.feature_names[0],bunchobject.feature_names[3])

