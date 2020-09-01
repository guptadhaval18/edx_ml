import numpy as np
from sklearn.svm import SVC # "Support Vector Classifier"
import matplotlib.pyplot as plt
X = np.array([[5,1,1],[5,2,1],[2,4,1],[4,4,1],[5,5,1],[0,0,-1],[2,0,-1],[3,0,-1],[0,2,-1],[2,2,-1]])
y = np.array([1,1,1,1,1,-1,-1,-1,-1,-1])
clf = SVC(kernel='linear')
clf.fit(X,y)
print(clf.coef_)
print(clf.score(X, y))

