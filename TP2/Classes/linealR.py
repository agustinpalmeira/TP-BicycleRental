import csv
import random
import scipy
import operator
import unicodedata
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

train = pd.read_csv("trainEditado3.csv", header=0, \
                      delimiter=",", quoting=2)
labels = train['duration']
train = train.drop(['duration'],1)
X_train, X_test, y_train, y_test = train_test_split(train, labels, test_size=0.4, random_state = 42)

regr = LinearRegression()

re = regr.fit(X_train, y_train)
#re = regr.fit(train, labels)
print regr.score(X_test, y_test)

#test= pd.read_csv("testEditado3.csv", header=0,delimiter=",", quoting=2)
#test2=test
#test = test.drop(['id'],1)
#lr_preds = regr.predict(test)
#output = pd.DataFrame( data={"Id":test2["id"], "duration":lr_preds} )
#output.to_csv( "submission29.csv", index=False, quoting=1 )
