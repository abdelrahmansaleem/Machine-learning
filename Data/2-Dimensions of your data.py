# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:42:12 2020

@author: Abd_Elrahman
"""

# Dimensions of your data
from pandas import read_csv
filename = "pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
shape = data.shape
print(shape)