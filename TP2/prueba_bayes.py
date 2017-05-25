from sklearn import datasets
from sklearn.feature_extraction.text import CountVectorizer
import re
import csv
import random
import scipy
import operator
import unicodedata
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import neighbors
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

train = pd.read_csv("trainEditado.csv", header=0, \
                      delimiter=",", quoting=2)

gnb = GaussianNB()
X = train["mean_temperature_f"]
X = X.reshape(-1, 1)
y_pred = gnb.fit(X, train["duration"]).predict(X)
print("Number of mislabeled points out of a total %d points : %d"  % (train.shape[0],(train["duration"] != y_pred).sum()))

# print "\nGenero csv para submission\n"
# output = pd.DataFrame( data={"Id":train["id"], "Prediction":y_pred} )
# output.to_csv( "prueba1SobreTrain.csv", index=False, quoting=2 )
