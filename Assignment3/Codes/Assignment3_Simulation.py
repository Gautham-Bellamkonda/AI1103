import numpy as np
import scipy 
import math
import matplotlib.pyplot as plt
from scipy.stats import norm
from random import random
simlen = int(1e6)
points = 60
beta = np.arange(-3.0,3.0, 6.0/points)
beta_i = -3.0
BER_sim = []
BER_Q = []
data = []
a = 6.069
    #create a gaussian r.v. for simulation
for i in range(0,points):
    #make a gaussian distribution of Z with mean betaX and compare it with -a and +a
    #1-> X = a
    count_1 = 0
    for j in range(0,simlen):
        elem = 0
        for k in range(1,11):
            elem = elem + random()
        elem = elem - 5 + beta_i*a
        if(elem < -a):                  
            count_1 = count_1 + 1
    prob_1 = count_1/(simlen)
    #2-> X = -a
    count_2 = 0
    for j in range(0,simlen):
        elem = 0
        for k in range(1,11):
            elem = elem + random()
        elem = elem - 5 - beta_i*a
        if(elem > a):
            count_2 = count_2 + 1
    prob_2 = count_2/(simlen)
    prob = (prob_1 + prob_2)/2
    BER_sim.append(prob)            
    beta_i = beta_i + 0.1          #incrementing
#Q function thereoretical
BER_Q = 1-norm.cdf(a*(1+beta), 0, 1)
plt.semilogy(beta, BER_sim, 'o')
plt.semilogy(beta, BER_Q, '-')
plt.plot([-0.3],[0.0000059], 'gx')
plt.plot([0.0],[0.0000000006], 'bo')
plt.text(-0.25,0.000005,r'$ ( \beta = -0.3$, BER = 6.7 $\times 10^{-6} ) $')
plt.grid()
plt.legend(["Simulated", "Theoretical"])
plt.title(r"Bit Error Rate (BER) for different values of $\beta$") 
plt.xlabel(r'$ \beta$ axis')
plt.ylabel("Bit Error Rate (BER)")
plt.show()
