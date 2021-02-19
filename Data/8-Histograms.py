# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:11:07 2020

@author: Abd_Elrahman
"""

# Univariate Histograms
from matplotlib import pyplot
from pandas import read_csv
filename = 'pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
data.hist()
pyplot.show()