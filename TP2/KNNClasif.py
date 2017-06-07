import csv
import random
import operator
import unicodedata
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score


train = pd.read_csv("trainEditado3.csv", header=0, \
                      delimiter=",", quoting=2)
print 'Lei archivo de train'
print 'KNN'
x=train[['start_station_id','mean_temperature_f','mean_wind_speed_mph']]
y=train['duration']

X_train, X_test, y_train, y_test = train_test_split(train, y, test_size=0.4, random_state=42)
knn = KNeighborsClassifier(n_neighbors=3)

kn = knn.fit(X_train, y_train)
print knn.score(X_test, y_test)
print "prediciendo"
test= pd.read_csv("testEditado3.csv", header=0, \
                       delimiter=",", quoting=2)
test2=test
test = test.drop(['id'],1)
knn_preds = knn.predict(test)
output = pd.DataFrame( data={"Id":test2["id"], "duration":knn_preds} )
output.to_csv( "submission14.csv", index=False, quoting=1 )
