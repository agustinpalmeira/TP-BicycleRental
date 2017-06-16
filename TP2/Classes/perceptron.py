#Reference http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron.fit

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
import pandas as pd

train = pd.read_csv("/Users/agustinpalmeira/Documents/Agus Varios/Facu/datos/tp2017/trainEditado.csv", header=0, delimiter=",", quoting=2)
print('Read csv')
labels = train['duration']
train = train.drop(['duration'], 1)
X_train, X_test, y_train, y_test = train_test_split(train, labels, test_size=0.2, random_state = 20)

print('Trainning...')

clf = Perceptron()
clf.fit(X_train, y_train)

print ('Finished Train...')

print('Accuracy:', clf.score(X_test, y_test))

print('Reading test CSV...')

test = pd.read_csv("/Users/agustinpalmeira/Documents/Agus Varios/Facu/datos/tp2017/testEditado.csv", header=0, delimiter=",", quoting=2)

print('Test CSV read...')

test2 = test
test = test.drop(['id'], 1)

print('...')

perceptronPredictor = clf.predict(test)

print('Generating output...')

output = pd.DataFrame(data={"Id": test2["id"], "duration": perceptronPredictor})

print('...')

output.to_csv("submissionsarasa.csv", index=False, quoting=1)