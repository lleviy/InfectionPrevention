data = [
    ['1', 1],
    ['2', 0.2],
    ['3', 0.5],
    ['4', 1],
    ['5', 0],
    ['6', 0],
    ['7', 0.7],
    ['8', 0],
    ['9', 0],
    ['10', 0]
]
X = []
y = []
for i in data:
    X.append(i[0])
    y.append(i[1])

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

from sklearn.linear_model import LinearRegression
import numpy as np
regressor = LinearRegression()
regressor.fit(X_vectorized, y)

test_feature = vectorizer.transform(['1'])
prediction = regressor.predict(test_feature)
print(prediction)
test_feature = vectorizer.transform(['3'])
prediction = regressor.predict(test_feature)
print(prediction)
test_feature = vectorizer.transform(['4'])
prediction = regressor.predict(test_feature)
print(prediction)

import pickle
pickl = {
    'vectorizer': vectorizer,
    'regressor': regressor
}

pickle.dump(pickl, open('models' + ".p", "wb"))

