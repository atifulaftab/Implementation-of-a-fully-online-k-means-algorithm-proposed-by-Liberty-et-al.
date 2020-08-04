# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:42:46 2018

@author: atifu
"""

from onlineKmeans import onlineKmeans

def cluster(data):
    list  = []
    for k in range (10, 50, 10):
        C  = onlineKmeans(data, k)
        list.append(len(C))
        return list