#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")

from email_preprocess import preprocess
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]
#labels_test = labels_test[:len(labels_test)/100]
#features_test = features_test[:len(features_test)/100]
print len(features_test)
t0 = time()
#clf = SVC(kernel='linear')
clf = SVC(C = 10000,kernel='rbf')
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t1, 3), "s"

accurcy = accuracy_score(labels_test,pred)
print "accurcy rate :",accurcy

print pred[10]
print pred[26]
print pred[50]



print len(pred)
count = 0
for i in pred:
    if i == 1:
        count=count+1

print count


#########################################################


