import csv
import random
import operator
import unicodedata
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import ExtraTreesRegressor

train = pd.read_csv("trainEditadoDist.csv", header=0, \
                      delimiter=",", quoting=2)
labels = train['duration']
train = train.drop(['duration'],1)

estimators = [10, 20, 30, 40, 50, 60]

cv_scores = []

for n in estimators:
	print "n_estimator = ", n	
	etr = ExtraTreesRegressor(n_estimators = n)
	scores = cross_val_score(etr, train, labels, cv=10)
	cv_scores.append(scores.mean())

error = [1 - x for x in cv_scores]

optimal_n = estimators[error.index(min(error))]
print "La cantidad de estimadores optima es: %d" % optimal_n
