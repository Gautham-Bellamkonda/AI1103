import numpy as np
from scipy.optimize import fmin
import math

def f(x): return x - x*x 
max_sim_x = fmin(lambda x: -f(x), 0)
max_sim = f(max_sim_x[0])
max_theoretical_x = 0.5
max_theoretical = f(max_theoretical_x)

print("Theoretical maximum value = ", max_theoretical)
print("Simulated maximum value = ", max_sim)