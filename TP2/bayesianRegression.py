from sklearn.model_selection import train_test_split
from sklearn import linear_model
import pandas as pd


#http://scikit-learn.org/stable/modules/linear_model.html#bayesian-regression

#Example:

#X = [[0., 0.], [1., 1.], [2., 2.], [3., 3.]]
#Y = [0., 1., 2., 3.]
#reg = linear_model.BayesianRidge()
#reg.fit(X, Y)
#reg.predict ([[1, 0.]])
#reg.coef_

train = pd.read_csv("trainEditado.csv", header=0, delimiter=",", quoting=2)
labels = train['duration']
train = train.drop(['duration'], 1)
X_train, X_test, y_train, y_test = train_test_split(train, labels, test_size=0.4, random_state = 42)

regr = linear_model.BayesianRidge()

re = regr.fit(X_train, y_train)

print regr.score(X_test, y_test)