from sklearn.model_selection import train_test_split
from sklearn import linear_model
import pandas as pd
from sklearn.metrics import mean_squared_error

#http://scikit-learn.org/stable/modules/linear_model.html#bayesian-regression

#Example:

#X = [[0., 0.], [1., 1.], [2., 2.], [3., 3.]]
#Y = [0., 1., 2., 3.]
#reg = linear_model.BayesianRidge()
#reg.fit(X, Y)
#reg.predict ([[1, 0.]])
#reg.coef_


print('Reading Train...')

train = pd.read_csv("trainEditado.csv", header=0, delimiter=",", quoting=2)
labels = train['duration']
train = train.drop(['duration'], 1)
X_train, X_test, y_train, y_test = train_test_split(train, labels, test_size=0.4, random_state = 42)

print('Generating Bayesian...')

regr = linear_model.BayesianRidge()

print('Fitting train...')

re = regr.fit(X_train, y_train)

print('...')

print('Accurancy:')

print regr.score(X_test, y_test)

print('Reading test CSV...')

test = pd.read_csv("testEditado7.csv", header=0, delimiter=",", quoting=2)

print('Test CSV read...')

test2 = test

print ('Drop...')

test = test.drop(['id'], 1)

bayesianPredictor = re.predict(test)

print('Generating Data Frame output...')

output = pd.DataFrame(data={"Id": test2["id"], "duration": bayesianPredictor})

print('Generating CSV output...')

output.to_csv("submissionBayesian2.csv", index=False, quoting=1)

y = output
y['id'] = y['Id'].astype(int)
y['duration'] = y['duration'] .astype(int)
aux = pd.read_csv("trip.csv", header=0,delimiter=",", quoting=2)

print('Merging...')

prueba = pd.merge(aux, y, how='inner', on='id')

print('Calculating Cuadratic Error...')

MSE = mean_squared_error(prueba['duration_x'], prueba['duration_y'])

print "Error cuadratico medio: ", MSE

#Error cuadratico medio:  43963182.7828