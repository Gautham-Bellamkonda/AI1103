import numpy as np
import scipy 
import math
import matplotlib.pyplot as plt
from scipy.stats import norm

a = 1
beta = 0.5
mean1 = a*(1+beta)
mean2 = -a*(1+beta)
standard_dev = 1
x = np.arange(-6,6, 0.001)
y1 = norm(mean1, standard_dev)
y2 = norm(mean2, standard_dev)
k = 0.0668072
x_values = [0.0, 0.0]
y_values = [k, 1-k]
plt.plot(x_values, y_values,'black')
plt.plot(x,y1.cdf(x))
plt.plot(x,y2.cdf(x))
plt.grid()


y_values = [0.0, k]
plt.plot(x_values, y_values,'x-')

y_values = [1-k, 1]
plt.plot(x_values, y_values,'x-')

plt.ylabel("$F_Y(y)$")
plt.xlabel("y - axis")
plt.legend(["Threshold of the detector","$F_Y(y , X =+a)$","$F_Y(y , X =-a)$", "BER$_{+a}$", "BER$_{-a}$"], prop={'size': 7})
plt.title("Representing BER in CDF of $Y$") 
plt.show()
