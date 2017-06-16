import csv
import random
import scipy
import operator
import unicodedata
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score


train = pd.read_csv("trainEditado.csv", header=0, \
                      delimiter=",", quoting=2)
labels = train['duration']
train = train.drop(['duration'],1)

k_list = list(range(1,50))

neighbors = filter(lambda x: x % 2 != 0, k_list)

cv_scores = []

for k in neighbors:
	knn = KNeighborsRegressor(n_neighbors = k)
	scores = cross_val_score(knn, train, labels, cv=10)
	cv_scores.append(scores.mean())

error = [1 - x for x in cv_scores]

optimal_k = neighbors[error.index(min(error))]
print "El k óptimo es: %d" % optimal_k
