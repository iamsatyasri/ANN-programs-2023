import numpy as np
import matplotlib.pyplot as plt

def binarysigmoid(x):
    return 1 / (1 + np.exp(-x))

X = np.linspace(-5, 5, 100)
plt.plot(X, binarysigmoid(X), 'b')
plt.show()
#Bipolar sigmoidal function
import numpy as np
import matplotlib.pyplot as plt

def bipolarsigmoid(x):
    return (1 - np.exp(-x)) / (1 + np.exp(-x))

X = np.linspace(-5, 5, 100)
plt.plot(X, bipolarsigmoid(X), 'b')
plt.show()
