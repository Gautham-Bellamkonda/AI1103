#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
#if using termux
import subprocess
import shlex
#end if


gamma = np.arange(0,10,0.1)#points on the x axis

def Pe(x):
    return 0.5 - 0.5*(math.sqrt(x/(2+x)))

vect_Pe = scipy.vectorize(Pe)
plt.plot(gamma, vect_Pe(gamma), '-')
plt.xlabel('$\gamma$')
plt.ylabel('$P_e(\gamma)$')
plt.grid()
#if using termux
#plt.savefig('figs/cond/Pe_vs_gamma.pdf')
#plt.savefig('figs/cond/Pe_vs_gamma.eps')
#subprocess.run(shlex.split("termux-open figs/cond/Pe_vs_gamma.pdf"))
#else
plt.show() #opening the plot window