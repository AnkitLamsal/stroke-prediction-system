import numpy as np
import pickle

filename = "model.sav"
model = pickle.load(open(filename, 'rb'))

X_test = np.array([0.862887,0.0,0.0,1.0,0.0,2.026336,1.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0,0.0,0.737943])

X_test = X_test.reshape(1,-1)

y_pred = model.predict(X_test)

print(y_pred)
