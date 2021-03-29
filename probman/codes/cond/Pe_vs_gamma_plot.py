#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
import scipy.stats as ss
#if using termux
import subprocess
import shlex
#end if


gamma = np.arange(0.00001,10,0.1)#points on the x axis

def Pe(x):
    return 0.5 - 0.5*(math.sqrt(x/(2+x)))

vect_Pe = scipy.vectorize(Pe)

#simulation
simlen = int(1e3)
N = np.random.normal(0,1,simlen)
prob = []

for i in range(0, 100):
    prob_sum = 0
    for j in range(simlen):
        prob_sum += ss.rayleigh.cdf(N[j], loc = 0, scale = math.sqrt((gamma[i])/2))
    prob_sum /= simlen
    prob.append(prob_sum)


plt.plot(gamma, vect_Pe(gamma), '-')
plt.plot(gamma, prob, 'o')
plt.xlabel('$\gamma$')
plt.ylabel('$P_e(\gamma)$')
plt.legend(["Theoretical", "Simulated"])
plt.grid()
#if using termux
#plt.savefig('figs/cond/Pe_vs_gamma.pdf')
#plt.savefig('figs/cond/Pe_vs_gamma.eps')
#subprocess.run(shlex.split("termux-open figs/cond/Pe_vs_gamma.pdf"))
#else
plt.show() #opening the plot window