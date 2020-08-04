# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:36:14 2018

@author: atifu
"""
import fileReading
import numpy as np

def dataprocess():
    data = fileReading.readFile('breast-cancer-wisconsin.data')
    data = data[:, :-1]
    data = np.array(data) 
    data = data.astype(float)
    return data