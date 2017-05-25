import csv
import random
import scipy
import operator
import unicodedata
import numpy as np
import pandas as pd
from sklearn import neighbors
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier


#ya esta con 2 columnas
train = pd.read_csv("trainEditado.csv", header=0, \
                      delimiter=",", quoting=2)
#train["duration"]= str(train["duration"])
print 'Lei archivo de train'

y=train["duration"]
x=train[["mean_temperature_f","mean_wind_speed_mph"]]
rf = RandomForestClassifier(n_estimators=100)
rf.fit(x,y)

scores =cross_val_score (rf,x,y,cv=10)
print ("Accuracy: % 0.2f (+/- %0.2f)" % (scores.mean(), scores.std() *2 ))

# # Utility function to report best scores
# def report(results, n_top=3):
#     for i in range(1, n_top + 1):
#         candidates = np.flatnonzero(results['rank_test_score'] == i)
#         for candidate in candidates:
#             print("Model with rank: {0}".format(i))
#             print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
#                   results['mean_test_score'][candidate],
#                   results['std_test_score'][candidate]))
#             print("Parameters: {0}".format(results['params'][candidate]))
#             print("")

# # specify parameters and distributions to sample from
# param_dist = {"max_depth": [3, None],
#               "max_features": sp_randint(1, 11),
#               "min_samples_split": sp_randint(1, 11),
#               "min_samples_leaf": sp_randint(1, 11),
#               "bootstrap": [True, False],
#               "criterion": ["gini", "entropy"]}

# # run randomized search
# n_iter_search = 20
# random_search = RandomizedSearchCV(clf, param_distributions=param_dist,
#                                    n_iter=n_iter_search)


# print "editando el csv de Test" ####HACERLO CON EL DE TEST
# test = pd.read_csv("trainEditado.csv", header=0, \
#                       delimiter=",", quoting=2)
# # # keep_column=['Id','Text']
# # new_f = test[keep_column]
# # new_f.to_csv("testEditado.csv", index=False)

# # test = pd.read_csv("testEditado.csv", header=0, \
# #                       delimiter=",", quoting=2)

# # print "Nuevo csv de test creado y leido"
# # num_test_reviews = len(test["Text"])
# # reviews_de_test_procesadas = [] 

# # for i in xrange(0,num_test_reviews):
# #     if( (i+1) % 2000 == 0 ):
# #         print "Review %d of %d\n" % (i+1, num_test_reviews)
# #     reviews_de_test_procesadas = procesar( test["Text"][i] )
# #     reviews_de_test_procesadas.append( reviews_de_test_procesadas )

# # test_features = vectorizer.transform(reviews_de_test_procesadas)              
# # test_features = test_features.toarray()


predicciones = rf.predict(x)
#output = pd.DataFrame( data={"Id":train["id"], "Prediction":predicciones} )
output = pd.DataFrame( data={"Prediction":predicciones} )
output.to_csv( "submission.csv", index=False, quoting=1 )
