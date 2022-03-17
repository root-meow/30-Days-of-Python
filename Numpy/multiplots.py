import numpy as np
from numpy.random import random
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi)
x = np.sin(t)
y = np.cos(t)

#To divide the plotting area
plt.subplot(2, 1, 1)
plt.plot(x)
plt.title('plot 1')

#now activate a new plotting area
plt.subplot(2, 1, 2)
plt.plot(y)
plt.title('plot 2')

plt.show() #test