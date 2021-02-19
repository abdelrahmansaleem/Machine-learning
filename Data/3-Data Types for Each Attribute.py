# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:42:31 2020

@author: Abd_Elrahman
"""

# Data Types for Each Attribute
from pandas import read_csv
filename = "pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
types = data.dtypes
print(types)