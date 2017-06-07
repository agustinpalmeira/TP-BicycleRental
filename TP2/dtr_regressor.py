import csv
import random
import scipy
import operator
import unicodedata
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

train = pd.read_csv("trainEditado3.csv", header=0, \
                      delimiter=",", quoting=2)
labels = train['duration']
train = train.drop(['duration'],1)
X_train, X_test, y_train, y_test = train_test_split(train, labels, test_size=0.2, random_state = 2)

#dtr = DecisionTreeRegressor(min_samples_leaf = 3,
#                            max_depth = 8,
#                            random_state = 2)

dtr = DecisionTreeRegressor()

dt = dtr.fit(X_train, y_train)

print dtr.score(X_test, y_test)

test= pd.read_csv("testEditado3.csv", header=0,delimiter=",", quoting=2)
test2=test
test = test.drop(['id'],1)
dtr_preds = dtr.predict(test)
output = pd.DataFrame( data={"Id":test2["id"], "duration":dtr_preds} )
output.to_csv( "submission20.csv", index=False, quoting=1 )
