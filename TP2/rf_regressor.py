import csv
import random
import scipy
import operator
import unicodedata
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

train = pd.read_csv("trainEditadoDist.csv", header=0, \
                      delimiter=",", quoting=2)
labels = train['duration']
train = train.drop(['duration'],1)
X_train, X_test, y_train, y_test = train_test_split(train, labels, test_size=0.4, random_state = 42)

rfr = RandomForestRegressor(n_estimators=150)
#rf = rfr.fit(X_train,y_train)
rf= rfr.fit(train, labels)
#print rfr.score(X_test, y_test)

test= pd.read_csv("testEditado7.csv", header=0,delimiter=",", quoting=2)
test2=test
test = test.drop(['id'],1)
rfr_preds = rfr.predict(test)
output = pd.DataFrame( data={"id":test2["id"], "duration":rfr_preds} )

#output.to_csv( "submission44.csv", index=False, quoting=1 )
y=output
y['id'] = y['id'].astype(int)
y['duration']= y['duration'] .astype(int)
aux= pd.read_csv("trip.csv", header=0,delimiter=",", quoting=2)
prueba = pd.merge(aux,y,how='inner', on='id')
MSE = mean_squared_error(prueba['duration_x'],prueba['duration_y'])
print "error cuadratico medio",MSE
