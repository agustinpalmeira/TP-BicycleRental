#Reference http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron.fit

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
import pandas as pd

train = pd.read_csv("trainEditado.csv", header=0, delimiter=",", quoting=2)
print('Read csv')
labels = train['duration']
train = train.drop(['duration'], 1)
X_train, X_test, y_train, y_test = train_test_split(train, labels, test_size=0.4, random_state = 42)

print('Begin Train')

clf = Perceptron()
clf.fit(X_train, y_train)

print ('Finished Train')

print('Accuracy:', clf.score(X_test, y_test))