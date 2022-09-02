from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
from random import shuffle

data = [([1], 0), ([2], 0), ([3], 1), ([6], 1), ([6], 1), ([7], 0), ([10], 0), ([11], 0)]
shuffle(data)
X = [d[0] for d in data]
y = [d[1] for d in data]

neigh.fit(X[0:4], y[0:4])

y_pred = neigh.predict(X[4:])
print("predictions: ", y_pred)
from sklearn.metrics import confusion_matrix
y_true = y[4:]
# y_pred = [0, 0, 2, 2, 0, 2]
confusion_matrix(y_true, y_pred)
