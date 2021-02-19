# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:59:15 2020

@author: Abd_Elrahman
"""

# Class Distribution
from pandas import read_csv
filename = "pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
class_counts = data.groupby('class').size()
print(class_counts)