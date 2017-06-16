import csv
import random
import scipy
import operator
import unicodedata
import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesRegressor

train = pd.read_csv("trainEditadoDist.csv", header=0, \
                      delimiter=",", quoting=2)
labels = train['duration']
train = train.drop(['duration'],1)
etr= ExtraTreesRegressor(n_estimators = 50)
etr = etr.fit(train, labels)

test= pd.read_csv("testEditado7.csv", header=0,delimiter=",", quoting=2)
test2=test
test = test.drop(['id'],1)
etr_preds = etr.predict(test)
output = pd.DataFrame( data={"Id":test2["id"], "duration":etr_preds} )
output.to_csv( "submission41.csv", index=False, quoting=1 )


