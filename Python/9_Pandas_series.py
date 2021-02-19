# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:09:25 2020

@author: Abd_Elrahman
"""

# series
import numpy
import pandas
myarray = numpy.array([1, 2, 3])
rownames = ['a', 'b', 'c']
myseries = pandas.Series(myarray, index=rownames)
print(myseries)
print(myseries[0])
print(myseries['a'])
