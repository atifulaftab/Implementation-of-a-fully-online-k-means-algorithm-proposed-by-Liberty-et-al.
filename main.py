# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 22:17:29 2018

@author: atifu
"""

import fileReading
import numpy as np
from onlineKmeans import onlineKmeans
from cluster import cluster
from sklearn import svm
from sklearn.model_selection import train_test_split


#data = fileReading.readFile('Skin_NonSkin.txt')
#labels = data[:, -1]
#data = data[:, :-1]
#data = np.array(data, dtype = float)
#np.random.shuffle(data)
#C = onlineKmeans(data, 20)

#data = fileReading.readFile(r'D:\OneDrive\U of M Courses\Online Algorithm\project\brca_metabric\data_RNA_Seq_expression_median_modified.txt')
#data = data.transpose()
#labels = fileReading.readFile(r'D:\OneDrive\U of M Courses\Online Algorithm\project\brca_metabric\data_clinical_sample.txt')
#labels =  labels[4:,:]
#patientIDInLabels =labels[1:,0]
#patientIDInExpression = data[1:, 0]

#finalLabels = []
#for patientID in patientIDInLabels:
#   ind = np.argwhere(patientIDInExpression == patientID)
#    finalLabels.append(labels[ind,5])


#data = fileReading.readFile('Skin.txt')
#data = np.array(data) 
#data = data.astype(float)
#C  = onlineKmeans(data, 20)
    
data = fileReading.readFile('breast-cancer-wisconsin.data')
data = data[:, :-1]
data = np.array(data) 
data = data.astype(float)


#X_train, X_test, y_train, y_test = train_test_split(data, data, test_size=0.3,random_state=109)
#clf = svm.SVC(kernel='linear')
#clf.fit(X_train, y_train)

list=cluster(data)
#list  = []
#for k in range (10, 50, 10):
#    C  = onlineKmeans(data, k)
#    print(k)
#    list.append(len(C))

