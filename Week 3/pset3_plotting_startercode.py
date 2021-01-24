#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Jan  7 15:49:03 2019

@author: norman_lee
"""

"""
data for Nov 2018
daily total rainfall in mm of rain 
"""

import math
import matplotlib.pyplot as plt

# -5 to 5, step 1
x_list = list(range(-5,6))
print(x_list)

def logistic(x):
    # to calculate logistic
    #for one x point
    y = 1/(1 + math.exp(-x))
    return y

def calculate_y(xpoints):
    # you need to call logistic()
    # use while loop for every x
    # use y.append()
    y = []
    # your code
    # Init Block
    pos = 0 # Zero is the index of the first element
    # Condition
    while pos < len(xpoints):
        # Block A
        y.append(logistic(xpoints[pos]))
        # Modify condition
        pos += 1
    #Block B
    return y

y_list = calculate_y(x_list)
plt.plot(x_list, y_list)
plt.scatter(x_list, y_list)
plt.ylabel("y values")
plt.xlabel("x values")
plt.title("Logistic Function")
plt.show()

daily_total_rainfall = [ 0.2, 
7.8,
0.4,
3.4,
0.4,
3.8,
12,
5.4,
1.6,
0,
0.8,
12.4,
2.4,
2,
4.6,
0.8,
18.4,
7.4,
20.6,
4,
13.2,
2,
4,
0,
4.8,
14.4,
9.6,
0,
5.6,
7.6 ] 



""" 
data for Jan 2018
mean temperature is in degrees C
""" 

mean_temperature = [
        24.8,
25.5,
26.5,
26.1,
26,
26.8,
26.9,
26.4,
27.2,
24.5,
23.9,
23.1,
23,
23.4,
25.2,
26.2,
27.2,
27.2,
26.9,
26.4,
27.2,
27.5,
26.8,
26.7,
26.6,
26.4,
27.1,
26.3,
27.7,
26.9,
27.3]
