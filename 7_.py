# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:58:12 2020

@author: Abd_Elrahman
"""

# basic line plot
import matplotlib.pyplot as plt
import numpy
myarray = numpy.array([1, 2, 3])
plt.plot(myarray)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()