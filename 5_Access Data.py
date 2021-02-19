# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:47:13 2020

@author: Abd_Elrahman
"""

# access values
import numpy
mylist = [[1, 2, 3], [3, 4, 5]]
myarray = numpy.array(mylist)
print(myarray)
print(myarray.shape)
print("First row: ",myarray[0])
print("Last row: ", myarray[-1])
print("Specific row and col: ", myarray[0, 2])
print("Whole col: ", myarray[:, 2])