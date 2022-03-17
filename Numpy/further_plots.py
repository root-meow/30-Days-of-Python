import numpy as np
import matplotlib.pyplot as plt
import time

x = np.linspace(0, 2*np.pi, 50)  #Create a sequence with 50 values starting 0 and ending at the value of 2*pi
#print(x)  #test
y1 = np.sin(x)  #y1 is the sin of x
y2 = np.sin(2*x)

#Create and plot
plt.figure()  #Creates the figure to plot on. Just draws us x and y
plt.title('Sin x | sin 2x')
#plt.plot(y1, 'g-^') #Plots the figure for y1
plt.plot(x, y1)
#time.sleep(30)
#plt.clf() #clears the figure
#plt.plot(x, y1,'ro')

#red dot-dash circle
plt.plot(x, y1, 'r-o')
plt.plot(x, y1, 'g-o', x, y2, 'b-+')
plt.legend(['sin(x)', 'sin(2x)'])


plt.show() #test
