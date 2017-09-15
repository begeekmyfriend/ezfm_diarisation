# coding=utf-8

__author__ = 'hou'

from sklearn import linear_model
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib
import numpy as np
import sys
import os
import wave
import mfcc

def label(samples, marks, duration):
	sam_per_sec = len(samples) / duration
	labels = np.zeros(len(samples), dtype=np.int)

	for i in range(0, len(marks)):
		begin_sec = marks[i][0]
		end_sec = marks[i][1]
		labels[int(begin_sec * sam_per_sec): int(end_sec * sam_per_sec)] = 1

	return labels

def lgr_train(X, y):
	logreg = linear_model.LogisticRegression()
	logreg.fit(X, y)
	return logreg

def svm_train(X, y):
	clf = svm.SVC()
	clf.fit(X, y)
	return clf

def knc_train(X, Y):
	knc = KNeighborsClassifier(n_neighbors=3)
	knc.fit(X, Y) 
	return knc

def run(input_wav, songs):
        f = wave.open(input_wav, "r")
        duration = f.getnframes() / f.getframerate()

        X = mfcc.extract(input_wav, duration)
	y = label(X, songs, duration)

	clf = svm_train(X, y)
        model = "model/" + input_wav.split('.')[0] + ".pkl"
	joblib.dump(clf, model)
        print "Train OK, " + model + " generated."
        return model
