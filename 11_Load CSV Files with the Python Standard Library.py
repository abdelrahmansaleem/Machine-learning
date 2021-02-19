# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:29:56 2020

@author: Abd_Elrahman
"""

# Load CSV Using Python Standard Library
import csv
import numpy
filename = 'pima-indians-diabetes.data.csv'
raw_data = open(filename, 'r')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('float')
print(data.shape)