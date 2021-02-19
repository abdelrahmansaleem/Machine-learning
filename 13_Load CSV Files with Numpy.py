# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 13:08:48 2020

@author: Abd_Elrahman
"""

# Load CSV using NumPy
from numpy import loadtxt
filename = 'pima-indians-diabetes.data.csv'
raw_data = open(filename, 'rb')
data = loadtxt(raw_data, delimiter=",")
print(data.shape)