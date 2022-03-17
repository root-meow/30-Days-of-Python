import numpy as np
#import matplotlib
import matplotlib.pyplot as plt

t = np.linspace(0,2*np.pi,50)
x = np.sin(t)
y = np.cos(t)

#Now create a figure
plt.figure()
#plot x in it
plt.plot(x, 'g-^', label='sin') 
plt.xlabel('radians')
plt.ylabel('amplitude')
#g-^ gives all the points a green color and marks them with an up-facing triangle

#Create a new figure
#plt.figure()
#Plot y
plt.plot(y, 'r-o', label='cos') #r-o gives all the points a red color and a circle

# Add a title
plt.title("Cos") 
plt.legend()
plt.show()