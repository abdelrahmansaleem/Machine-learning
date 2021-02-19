# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 13:10:29 2020

@author: Abd_Elrahman
"""

# Load CSV using Pandas
from pandas import read_csv
filename = 'pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
print(data.shape)