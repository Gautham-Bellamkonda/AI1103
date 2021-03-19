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
x_values = [0.0, 0.0]
y_values = [0.0, 0.5]
plt.plot(x_values, y_values, color = 'black')
plt.plot(x,y1.pdf(x))
plt.plot(x,y2.pdf(x))
plt.grid()

plt.ylabel("$\Pr(Y=y)$")
plt.xlabel("y - axis")
plt.fill_between(x,0,y1.pdf(x),where=y1.pdf(x) < y2.pdf(x),color='C0', alpha = 0.4, interpolate=True)
plt.fill_between(x,0,y2.pdf(x),where=y2.pdf(x) < y1.pdf(x),color='C1', alpha = 0.4, interpolate=True)
plt.legend(["Threshold of the detector","$\Pr(Y=y , X =+a)$","$\Pr(Y=y , X =-a)$", "BER$_{+a}$", "BER$_{-a}$"], prop={'size': 7})
plt.title("Representing BER as area under a graph") 
plt.show()
