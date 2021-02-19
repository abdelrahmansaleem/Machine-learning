# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:05:11 2020

@author: Abd_Elrahman
"""

# basic scatter plot
import matplotlib.pyplot as plt
import numpy
x = numpy.array([1, 2, 3])
y = numpy.array([2, 4, 6])
plt.scatter(x,y)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()