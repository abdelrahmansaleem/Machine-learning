# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:13:28 2020

@author: Abd_Elrahman
"""

# dataframe
import numpy
import pandas
myarray = numpy.array([[1, 2, 3], [4, 5, 6]])
rownames = ['a', 'b']
colnames = ['one', 'two', 'three']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)
print("method 1:")
print("one column:  ", mydataframe['one'])
print("method 2:")
print("one column:  ", mydataframe.one)