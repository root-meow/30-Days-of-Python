import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt


N = 50 #Number of points we would like to have
x = np.linspace(0, 10, N)  #Create a series of values

e = rand(N)*5.0 #Noise
y1 = x + e

areas = rand(N)*300
plt.scatter(x, y1, s=areas) #s = float or array-like, shape
colors = rand(N)
plt.scatter(x, y1, s=areas, c=colors)
plt.colorbar()
plt.title("Random Scatter")
plt.show()
