import numpy as np
import scipy 
import math
import matplotlib.pyplot as plt
from scipy.stats import norm
from random import random
simlen = int(1e4)
points = 60
beta = np.arange(-3.0,3.0, 6.0/points)
beta_i = -3.0
BER_sim = []
BER_Q = []
data = []
a = 6.069
    #create a gaussian r.v. for simulation
for i in range(0,points):

    err_1 = 0
    for j in range(0,simlen):
        elem = 0
        for k in range(1,11):
            elem = elem + random()
        elem = elem - 5 + beta_i*a
        if(elem < -a):
            err_1 = err_1 + 1
    err_n1 = err_1/(simlen)
    err_2 = 0
    for j in range(0,simlen):
        elem = 0
        for k in range(1,11):
            elem = elem + random()
        elem = elem - 5 - beta_i*a
        if(elem > a):
            err_2 = err_2 + 1
    err_n2 = err_2/(simlen)
    err_n = (err_n1 + err_n2)/2
    BER_sim.append(err_n)
    beta_i = beta_i + 0.1
#Q function thereoretical
BER_Q = 1-norm.cdf(a*(1+beta), 0, 1)
plt.plot(beta, BER_sim, 'o')
plt.plot(beta, BER_Q, '-')
plt.grid()
plt.legend(["Simulated", "Theoretical"])
plt.title(r"Bit Error Rate (BER) for different values of $\beta$") 
plt.xlabel(r'$ \beta$ axis')
plt.ylabel("Bit Error Rate (BER)")
plt.show()









