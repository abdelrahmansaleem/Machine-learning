# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 13:15:37 2020

@author: Abd_Elrahman
"""

# View first 20 rows
from pandas import read_csv
filename = "pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
peek = data.head(20)
print(peek)