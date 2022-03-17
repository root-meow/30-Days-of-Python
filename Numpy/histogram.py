import numpy as np
from numpy.random import randint
import matplotlib.pyplot as plt

#create an array of data
data = randint(10000, size = (10,1000))

#approximate norm distribution
x = np.sum(data, axis=0)

#set up for stacked plots
plt.subplot(2, 1, 1)
plt.hist(x, color='r')
plt.title('Histogram 1')
#plot cumulative dist
plt.subplot(2, 1, 1)
plt.hist(x, cumulative=True)
plt.title('Histogram 2')


#For multiple histograms
#plt.hist([d1, d2])
plt.show()