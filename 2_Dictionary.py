# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:23:33 2020

@author: Abd_Elrahman
"""

mydict = {'a': 1, 'b': 2, 'c': 3}
print("A value: ", mydict['a'])
mydict['a'] = 11
print("A value: ", mydict['a'])
print("Keys: ",mydict.keys())
print("Values: ", mydict.values())
for key in mydict.keys():
    print (mydict[key])