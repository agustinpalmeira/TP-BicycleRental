import csv
import random
import scipy
import operator
import unicodedata
import numpy as np
import pandas as pd
from sklearn import neighbors


#ya esta con 2 columnas
train = pd.read_csv("trainEditado.csv", header=0, \
                      delimiter=",", quoting=2)
print 'Lei archivo de train'
print 'KNN'

###########

###########

x=train[['mean_temperature_f','mean_wind_speed_mph']]
y=train['duration']

	
knn = neighbors.KNeighborsClassifier(3)
knn.fit(x, y) 



print "prediciendo"
test= pd.read_csv("testEditado.csv", header=0, \
                      delimiter=",", quoting=2)
test2=test
test = test.drop(['id'],1)
rfr_preds = knn.predict(test)


###

###
output = pd.DataFrame( data={"Id":test2["id"], "duration":rfr_preds} )
output.to_csv( "submissionKNN.csv", index=False, quoting=1 )
