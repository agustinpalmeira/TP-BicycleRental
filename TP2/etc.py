import csv
import random
import scipy
import operator
import unicodedata
import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import mean_squared_error

train = pd.read_csv("trainEditadoDist.csv", header=0, \
                      delimiter=",", quoting=2)
labels = train['duration']
train = train.drop(['duration'],1)
etc= ExtraTreesRegressor()
et = etc.fit(train, labels)

test= pd.read_csv("testEditado7.csv", header=0,delimiter=",", quoting=2)
test2=test
test = test.drop(['id'],1)
etc_preds = etc.predict(test)
output = pd.DataFrame( data={"Id":test2["id"], "duration":etc_preds} )
output.to_csv( "submission41.csv", index=False, quoting=1 )

#y=output
#y['id'] = y['id'].astype(int)
#y['duration']= y['duration'] .astype(int)
#aux= pd.read_csv("/home/florencia/Datos/Data/sf-bay-area-bike-share/trip.csv", header=0,delimiter=",", quoting=2)
#prueba = pd.merge(aux,y,how='inner', on='id')
#MSE = mean_squared_error(prueba['duration_x'],prueba['duration_y'])
#print "error cuadratico medio",MSE
