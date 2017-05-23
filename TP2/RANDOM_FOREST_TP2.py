from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import re
import numpy as np
import pandas as pd

#ya esta con 2 columnas
train = pd.read_csv("trainEditado.csv", header=0, \
                      delimiter=",", quoting=2)
cant_trips = len(train["duration"])
trips_procesados = []                                                      
print "\nLeo archivo de train\n"
for i in xrange(0,cant_trips):
    if( (i+1) % 3000 == 0 ):
        print "Trip %d of %d\n" % (i+1, cant_trips)
    trips_procesados.append( train["mean_temperature_f"][i] )                          

# print "\nCreo BOW con scikit-learn\n"
# vectorizer = CountVectorizer(analyzer = "word",   \
#                              tokenizer = None,    \
#                              preprocessor = None, \
#                              stop_words = None,   \
#                              max_features = 500) 
# train_features = vectorizer.fit_transform(trips_procesados) #transforma los datos a feature vectors
# del trips_procesados

# train_features = train_features.toarray() ##si?
print "\nEntrenamiento del Random Forest\n"
rf = RandomForestClassifier(n_estimators = 100) 
forest = rf.fit( trips_procesados, train["duration"] )

scores = cross_val_score(rf,train_features ,train["duration"] , cv=10) #k=10 fold cross validation
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

# print "\nLeo Archivo de test\n"
# #ya esta con 2 columnas
# test = pd.read_csv("testEditado.csv", header=0, \
#                       delimiter=",", quoting=2)

# long_test = len(test["Text"])
# reviews_procesadas = [] 

# for i in xrange(0,long_test):
#     if( (i+1) % 2000 == 0 ):
#         print "Review %d of %d\n" % (i+1, long_test)
#     review_procesada = procesar( test["Text"][i] )
#     reviews_procesadas.append( review_procesada )

# test_features = vectorizer.transform(reviews_procesadas)              
# test_features = test_features.toarray()

# print "\nPrediciendo con el RandomForest\n"
# resultado = forest.predict(test_features)

# print "\nGenero csv para submission\n"
# output = pd.DataFrame( data={"Id":test["Id"], "Prediction":result} )
# output.to_csv( "SampleSubmission.csv", index=False, quoting=2 )