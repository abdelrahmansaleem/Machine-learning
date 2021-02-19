# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:31:19 2020

@author: Abd_Elrahman
"""

# Feature Extraction with RFE
from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
# load data
filename = 'pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
# feature extraction
model = LogisticRegression()
rfe = RFE(model, 3)
fit = rfe.fit(X, Y)
print("Num Features: ",fit.n_features_)
print("Selected Features: ",  fit.support_)
print("Feature Ranking:  ",fit.ranking_)