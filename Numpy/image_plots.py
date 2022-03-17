#Create some data
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt

e1 = rand(100)
e2 = rand(100) * 2
e3 = rand(100) * 3
e4 = rand(100) * 100

corrmatrix = np.corrcoef([e1, e2, e3, e4])

#Plot corr matrix as an image
plt.imshow(corrmatrix, cmap = 'GnBu')
plt.colorbar()
plt.show()